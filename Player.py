from typing import Tuple 

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board) -> Tuple[int, int]:
        raise NotImplementedError 