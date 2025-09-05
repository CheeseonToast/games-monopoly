# Copyright Gary Roberson 2024

import json
import os


class Content:
	def __init__(self):
		self._content = None


class DictContent(Content):
	def __init__(self, json_to_find):
		super().__init__()
		self.config_file_name = json_to_find
		self._content = self.load_content()

	@staticmethod
	def get_config_path(json_to_find):
		current_file = os.path.abspath(__file__)
		current_dir = os.path.abspath(os.path.join(current_file, os.path.pardir))
		file_found = False
		while not file_found:
			file_path = os.path.abspath(os.path.join(current_dir, "resources", json_to_find))
			file_found = os.path.isfile(file_path)
			if not file_found:
				old_dir = current_dir
				current_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
				if current_dir == old_dir:
					print(f"Could not find config.yaml anywhere from the path {current_dir}")
					raise Exception(f"Could not find config.yaml anywhere from the path {current_dir}")
		folder = os.path.join(current_dir, "resources")
		return folder

	def load_content(self):
		file = os.path.join(self.get_config_path(self.config_file_name), self.config_file_name)
		with open(file, 'r') as file:
			self._content = json.load(file)
			return self._content


class PropertyDataParser(DictContent):
	def __init__(self):
		super().__init__("../../resources/site_data.json")
		self.buildable_property = self._content["buildable_property"]
		self.non_buildable_property = self._content["non_buildable_property"]
		self.community_chests = self._content["community_chests"]
		self.chances = self._content["chances"]
		self.jail = self._content["jail"]
		self.tax = self._content["tax"]
		self.free_parking = self._content["free_parking"]
		self.go = self._content["go"]
		self.street_data = {}
		self.collate_sites_data()


	def collate_sites_data(self):
		self.collate_buildable_property()
		self.collate_non_buildable_property()
		self.collate_community_chests()
		self.collate_chances()
		self.collate_jail()
		self.collate_tax()
		self.collate_free_parking()
		self.collate_go()


		# Sort street_data by numeric key values
		sorted_keys = sorted(self.street_data.keys(), key=lambda x: int(x))
		self.street_data = {k: self.street_data[k] for k in sorted_keys}

		return

	def collate_buildable_property(self):
		for k, v in self.buildable_property.items():
			property_data = { k: {
				"name": self.buildable_property[k]["site_name"],
				"site_position": self.buildable_property[k]["site_position"],
				"site_cost": self.buildable_property[k]["site_cost"],
				"building_cost": self.buildable_property[k]["building_cost"],
				"site_rent": self.buildable_property[k]["site_rent"]
			}}
			self.street_data.update(property_data)
		return

	def collate_non_buildable_property(self):
		for k, v in self.non_buildable_property.items():
			property_data = { k: {
				"name": self.non_buildable_property[k]["site_name"],
				"site_position": self.non_buildable_property[k]["site_position"],
				"site_cost": self.non_buildable_property[k]["site_cost"],
				"site_rent": self.non_buildable_property[k]["site_rent"]
			}}
			self.street_data.update(property_data)

	def collate_community_chests(self):
		for k, v in self.community_chests.items():
			property_data = { k: {
				"name": self.community_chests[k]["site_name"],
				"site_position": self.community_chests[k]["site_position"]
			}}
			self.street_data.update(property_data)

	def collate_chances(self):
		for k, v in self.chances.items():
			property_data = { k: {
				"name": self.chances[k]["site_name"],
				"site_position": self.chances[k]["site_position"]
			}}
			self.street_data.update(property_data)

	def collate_jail(self):
		for k, v in self.jail.items():
			if "Jail" in v:
				property_data = { k: {
					"name": self.jail[k]["site_name"],
					"site_position": self.jail[k]["site_position"],
					"currently_in_jail": []
				}}
			else:
				property_data = { k: {
					"name": self.jail[k]["site_name"],
					"site_position": self.jail[k]["site_position"]
				}}
			self.street_data.update(property_data)

	def collate_tax(self):
		for k, v in self.tax.items():
			property_data = { k: {
				"name": self.tax[k]["site_name"],
				"site_position": self.tax[k]["site_position"],
				"tax_amount": self.tax[k]["tax_amount"]
			}}
			self.street_data.update(property_data)

	def collate_free_parking(self):
		for k, v in self.free_parking.items():
			property_data = { k: {
				"name": self.free_parking[k]["site_name"],
				"site_position": self.free_parking[k]["site_position"],
				"free_parking_amount": self.free_parking[k]["free_parking_amount"]
			}}
			self.street_data.update(property_data)

	def collate_go(self):
		for k, v in self.go.items():
			property_data = { k: {
				"name": self.go[k]["site_name"],
				"site_position": self.go[k]["site_position"],
				"reward": self.go[k]["reward"]
			}}
			self.street_data.update(property_data)



class PropertyData(PropertyDataParser):
	def __init__(self, site: int):
		super().__init__()
		self.name = self.street_data[str(site)]["name"]
		self.cost = self.street_data[str(site)]["cost"]
		self.house_cost = self.street_data[str(site)]["house_cost"]
		self.hotel_cost = self.street_data[str(site)]["hotel_cost"]
		self.base_rent = self.street_data[str(site)]["base_rent"]
		self.set_rent = self.street_data[str(site)]["set_rent"]
		self.house_1_rent = self.street_data[str(site)]["house_1_rent"]
		self.house_2_rent = self.street_data[str(site)]["house_2_rent"]
		self.house_3_rent = self.street_data[str(site)]["house_3_rent"]
		self.house_4_rent = self.street_data[str(site)]["house_4_rent"]
		self.hotel_rent = self.street_data[str(site)]["hotel_rent"]


class GameData(DictContent):
	def __init__(self):
		game_data_path = "../../../resources/game_data.json"
		super().__init__(game_data_path)
		self.houses = self._content["house_count"]
		self.hotels = self._content["hotel_count"]
		self.chance_cards_count = self._content["chance_cards"]
		self.community_chest_cards_count = self._content["community_chest_cards"]
		self.starting_money = self._content["starting_money"]
		self.sites = self._content["sites"]
		self.sites_type_list = self._content["site_type"]
		self.dice = self._content["dice"]
		self.players = []
