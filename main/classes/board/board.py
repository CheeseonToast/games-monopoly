# Copyright Gary Roberson 2024

from main.classes.street.street import *
from main.classes.game.game import GameData
from typing import List


class Board(GameData):
    def __init__(self):
        super().__init__()
        self.streets: List[Property] = []
        self.populate_streets()

    def populate_streets(self):
        if len(self.streets) == 0:
            i = 0
            for site_type in self.sites_type_list:
                if site_type in [1]:
                    street_gen = Property(site_type, i)
                    i += 1
                    self.streets.append(street_gen)
