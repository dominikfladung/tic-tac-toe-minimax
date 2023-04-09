"""
This module contains the class "InputPlayer"
"""

from typing import Tuple
from players.player import Player
from board import Board


class InputPlayer(Player):
    """
    A class to represent a Tic Tac Toe player that prompts the user to enter 
    coordinates for a move on
    """

    def move(self, board: Board) -> Tuple[int, int]:
        """
        This function prompts the user to enter coordinates for a move on a board and returns the
        coordinates if they are valid, otherwise it prints an error message and recursively calls
        itself.
        """
        user_input = input("Enter cordinates (x,y): ")
        cordinates = user_input.split(",")
        x = int(cordinates[0])
        y = int(cordinates[1])

        if board.is_valid_move(y, x):
            return x, y
        else:
            print("Invalid move!")
            return self.move(board)
