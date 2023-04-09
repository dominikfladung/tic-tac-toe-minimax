"""
Player class for Tic-Tac-Toe game.
"""
from abc import abstractmethod
from typing import Tuple


class Player:
    """
    A class to represent a Tic Tac Toe player.
    """
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


    @abstractmethod
    def move(self, board) -> Tuple[int, int]:
        """
        This function is called by the Game class to get the next move of the player.
        """
        raise NotImplementedError
