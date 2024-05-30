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
        super().__init__("../../resources/property_data.json")
        self.names = self._content["('Property', 'UK/International')"]
        self.cost = self._content["('Cost', 'Cost')"]
        self.base_rent = self._content["('Rent', 'Site')"]
        self.set_rent = self._content["('Rent', 'Site with colour set')"]
        self.house_1_rent = self._content["('Rent', '1 house')"]
        self.house_2_rent = self._content["('Rent', '2 houses')"]
        self.house_3_rent = self._content["('Rent', '3 houses')"]
        self.house_4_rent = self._content["('Rent', '4 houses')"]
        self.hotel_rent = self._content["('Rent', 'Hotel')"]
        self.house_cost = self._content["('Per House/Hotel Cost', 'Per House/Hotel Cost')"]
        self.hotel_cost = self._content["('Per House/Hotel Cost', 'Per House/Hotel Cost')"]  # In case of house rules
        self.street_data = None
        self.collate_street_data()

    def collate_street_data(self):
        self.street_data = {}
        for val, key in self.names.items():
            t_tuple = {val: {"name": self.names[str(val)],
                             "cost": self.cost[str(val)],
                             "house_cost": self.house_cost[str(val)],
                             "hotel_cost": self.hotel_cost[str(val)],
                             "base_rent": self.base_rent[str(val)],
                             "set_rent": self.set_rent[str(val)],
                             "house_1_rent": self.house_1_rent[str(val)],
                             "house_2_rent": self.house_2_rent[str(val)],
                             "house_3_rent": self.house_3_rent[str(val)],
                             "house_4_rent": self.house_4_rent[str(val)],
                             "hotel_rent": self.hotel_rent[str(val)]}
                       }
            self.street_data.update(t_tuple)
        return self.street_data


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
