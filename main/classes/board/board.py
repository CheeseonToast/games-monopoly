# Copyright Gary Roberson 2024

from main.classes.site.sites import *
from main.classes.game.game import GameData
from typing import List


class Board(GameData):
    def __init__(self):
        super().__init__()
        self.sites: List[Property] = []
        self.populate_streets()

    def populate_streets(self):
        if len(self.sites) == 0:
            i = 0
            for site_type in self.sites_type_list:
                if site_type in [1]:
                    street_gen = Property(site_type, i)
                    i += 1
                    self.sites.append(street_gen)
