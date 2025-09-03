# Copyright Gary Roberson 2024

from main.enum.street_enum import *
from utils.data_parser.data_parser import PropertyData
import math


class Site:
    def __init__(self, street_type: int, site_position: int):
        self._street_type = StreetType(street_type)
        self._site_position = site_position
        self._owner = None
        self.name = None
        self.mortgage_value = 0

    #  Setters
    def set_type(self, i):
        self._street_type = StreetType(i)

    #  Getters
    def get_type(self):
        return self._street_type

    def set_mortgage_value(self, i):
        self.mortgage_value = math.ceil(i/2)


class Property(Site):
    def __init__(self, street_type: int = 0, site_position: int = 0, colour=(255, 255, 255)):
        super().__init__(street_type, site_position)
        self.data = PropertyData(site_position)
        self.set_mortgage_value(self.data.cost)
        self.cost = self.data.cost
        self.name = self.data.name
        self.colour = colour
        self.houses = 0
        self.hotel = 0
        self.houses_cost = self.data.house_cost
        self.hotel_cost = self.data.hotel_cost
        self.rent = None
        self.set_rent(6)

    def remove_houses(self, i):
        self.houses = self.houses - i
        if self.houses < 0:
            return "houses was set to less than 0, this should never happen"

    def add_houses(self, i):
        self.houses = self.houses + i
        self.set_rent(self.houses)

        if self.houses > 4:
            return "houses was set to greater than 4, this should never happen"

    def add_hotel(self):
        if self.houses == 4:
            self.hotel = self.hotel + 1
            self.remove_houses(4)

    def remove_hotel(self):
        self.hotel = self.hotel - 1
        self.add_houses(4)

    def set_rent(self, rent):
        match rent:
            case 1:
                self.rent = self.data.house_1_rent
            case 2:
                self.rent = self.data.house_2_rent
            case 3:
                self.rent = self.data.house_3_rent
            case 4:
                self.rent = self.data.house_4_rent
            case 5:
                self.rent = self.data.hotel_rent
            case 6:
                self.rent = self.data.base_rent
            case 7:
                self.rent = self.data.set_rent

    def get_rent(self):
        return self.rent


class DrawCard(Site):
    def __init__(self, street_type: int, site_position: int, chance: bool = False):
        super().__init__(street_type, site_position)
        if chance:
            self._drawType = DrawType(0)
        else:
            self._drawType = DrawType(1)


class Tax(Site):
    def __init__(self, street_type: int, site_position: int, super_tax: bool = False):
        super().__init__(street_type, site_position)
        if super_tax:
            self._drawType = TaxType(1)
        else:
            self._drawType = TaxType(0)


class FreeParking(Site):
    def __init__(self, street_type: int, site_position: int):
        super().__init__(street_type, site_position)
        self._money = 0

    def get_money(self):
        return self._money

    def add_money(self, money):
        self._money = self._money + money

