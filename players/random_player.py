"""
This module contains the class "RandomPlayer"
"""

from typing import Tuple
import numpy as np
from players.player import Player


class RandomPlayer(Player):
    """
    A class to represent a Tic Tac Toe player that 
    randomly selects a valid move on the board.
    """

    def move(self, board) -> Tuple[int, int]:
        """
        This function randomly selects a valid move on a given board and returns the corresponding
        coordinates.
        """
        moves = board.get_valid_moves()
        y, x = moves[np.random.randint(0, len(moves))]
        return x, y
