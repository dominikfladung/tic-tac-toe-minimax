import numpy as np
from Player import Player
from typing import Tuple

class RandomPlayer(Player):
    def move(self, board) -> Tuple[int, int]:
        """
        This function randomly selects a valid move on a given board and returns the corresponding
        coordinates.
        
        :param board: The "board" parameter is likely an object representing the game board state. The
        method "get_valid_moves()" is likely a method of this object that returns a list of valid moves
        that the current player can make on the board. The method "move()" takes this board object as
        input and returns a
        :return: a tuple of two integers, representing the coordinates of a move on the board. The first
        integer represents the column number and the second integer represents the row number.
        """
        moves = board.get_valid_moves()
        y, x = moves[np.random.randint(0, len(moves))]
        return x, y