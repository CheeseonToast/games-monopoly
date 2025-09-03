# Copyright Gary Roberson 2024

from enum import Enum


class SiteType(Enum):
    GO = 0
    PROPERTY = 1
    JAIL = 2
    FREE_PARKING = 3
    TAX = 4
    DRAW_CARD = 5
    GO_TO_JAIL = 6


class SiteStatus(Enum):
    AVAILABLE = 0
    SOLD = 1
    MORTGAGE = 2


class DrawType(Enum):
    CHANCE = 0
    COMMUNITY_CHEST = 1


class TaxType(Enum):
    INCOME_TAX = 0
    SUPER_TAX = 1

