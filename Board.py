"""
This module contains the Board class, which represents the game board for a tic-tac-toe game.
"""

from players.player import Player
from copy import deepcopy
import numpy as np


class Board:
    """
    The Board class represents the game board for a tic-tac-toe game.
    """

    def __init__(self, x=3, y=3) -> None:
        self.map = np.zeros((y, x), dtype=int)

    def __str__(self) -> str:
        return str(self.map)

    def __getitem__(self, key):
        return self.map[key]

    def __setitem__(self, key, value):
        self.map[key] = value

    def __len__(self) -> int:
        return len(self.map)

    def copy(self):
        """
        copy() returns a deep copy of the board object.
        """
        return deepcopy(self)

    def is_full(self):
        """
        is_full() returns True if the board is full, and False otherwise.
        """
        return not 0 in self.map

    def is_valid_move(self, row, col):
        """
        is_valid_move() returns True if the move is valid, and False otherwise.
        """
        return self.map[row, col] == 0

    def make_move(self, row, col, player: Player):
        """
        This function makes a move on a game board for a given player at a specified row and column.
        """

        if not self.is_valid_move(row, col):
            raise Exception("Invalid move!")

        self.map[row, col] = player.symbol

    def get_valid_moves(self):
        """
        This function returns the indices of all valid moves in a game represented by a numpy array
        where 0 indicates an empty space.
        """
        return np.argwhere(self.map == 0)

    def get_winner(self):
        """
        This function checks if there is a winner in a game by checking the columns, rows, and
        diagonals.
        """
        is_winner_column = self.get_winner_column()
        is_winner_row = self.get_winner_row()
        is_winner_diagonal = self.get_winner_diagonal()

        return is_winner_column or is_winner_row or is_winner_diagonal or 0

    def get_winner_column(self):
        """
        This function checks the columns of a matrix to see if there is a winner and returns 
        the winning symbol or 0 if there is no winner.
        """
        for col in self.map.T:
            symbol = col[0]
            for row in col:
                if row != symbol:
                    symbol = None
                    break

            if symbol is not None and symbol != 0:
                return symbol

        return 0

    def get_winner_row(self):
        """
        This function checks if there is a winner in any row of a game map and returns the symbol of the
        winner or 0 if there is no winner.
        :return: the symbol of the player who has won the game by filling an entire row with their
        symbol. If no player has won, the function returns 0.
        """
        for row in self.map:
            symbol = row[0]
            for col in row:
                if col != symbol:
                    symbol = None
                    break

            if symbol is not None and symbol != 0:
                return symbol

        return 0

    def get_winner_diagonal(self):
        """
        This function checks if there is a winner in the diagonal lines of a game board.
        :return: This function returns the symbol of the player who has won the game diagonally, if
        there is a winner. If there is no winner, it returns 0.
        """
        symbol = self.map[0, 0]
        width = len(self.map[0])
        for i in range(len(self.map)):
            if i < width and self.map[i, i] != symbol:
                symbol = None
                break

        if symbol is not None and symbol != 0:
            return symbol

        symbol = self.map[0, width - 1]
        for i in range(len(self.map) - 1):
            if i < width and self.map[i, width - 1 - i] != symbol:
                symbol = None
                break

        if symbol is not None and symbol != 0:
            return symbol

        return 0

    def is_game_over(self):
        """
        The function checks if the game is over by determining if the board is full 
        or if there is a winner.
        """
        is_full = self.is_full()
        winner = self.get_winner()
        return is_full or winner != 0
