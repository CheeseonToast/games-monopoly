# Copyright Gary Roberson 2024

class Player(object):
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.money = 0
        self.owned_properties = {}
        self.mortgaged_properties = {}
        self.get_out_of_jail_cards = {}