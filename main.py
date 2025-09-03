# Copyright Gary Roberson 2024

from main.classes.game.game import *
from main.classes.board.board import *


class Main:
    def __init__(self):
        self.game_state = GameState()
        self.game_data = GameData()
        self.board = Board()


if __name__ == '__main__':
    main = Main()
    print(main.board.streets[1].name)
