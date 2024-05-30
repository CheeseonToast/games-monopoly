# Copyright Gary Roberson 2024

from utils.data_parser.data_parser import DictContent


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


class GameState(GameData):
    def __init__(self):
        super().__init__()

    # Houses
    def remove_houses(self, i):
        self.houses = self.houses - i

    def add_houses(self, i):
        self.houses = self.houses + i

    def get_houses(self):
        return self.houses

    # Hotels
    def remove_hotels(self, i):
        self.hotels = self.hotels - i

    def add_hotels(self, i):
        self.hotels = self.hotels + i

    def get_hotels(self):
        return self.hotels

    def get_starting_money(self):
        return self.starting_money

    def get_sites(self):
        return self.sites

    def get_num_dice(self):
        return self.dice

    # Draw cards
    def get_chance_cards_count(self):
        return self.chance_cards_count

    def get_community_chest_cards_count(self):
        return self.community_chest_cards_count

