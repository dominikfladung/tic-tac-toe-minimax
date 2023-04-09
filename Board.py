import numpy as np
from Player import Player
from copy import deepcopy

# The above class is named "Board" and likely contains methods and attributes related to a game board.
class Board:
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
        return deepcopy(self)

    def is_full(self):
        return not 0 in self.map

    def is_valid_move(self, row, col):
        return self.map[row, col] == 0

    def make_move(self, row, col, player: Player):
        """
        This function makes a move on a game board for a given player at a specified row and column.
        
        :param row: The row index of the cell where the player wants to make a move
        :param col: The column index of the move being made on the game board
        :param player: Player is a parameter of type Player, which represents the player making the
        move. It is assumed that the Player class has a property called "symbol" which represents the
        symbol (e.g. "X" or "O") that the player uses to mark their moves on the game board. The make
        :type player: Player
        """
        if not self.is_valid_move(row, col):
            raise Exception("Invalid move!")
        
        self.map[row, col] = player.symbol
        
    def get_valid_moves(self):
        """
        This function returns the indices of all valid moves in a game represented by a numpy array
        where 0 indicates an empty space.
        :return: The function `get_valid_moves` is returning the indices of all the empty cells in the
        `self.map` numpy array. Specifically, it is returning a numpy array of shape `(n, 2)` where `n`
        is the number of empty cells and each row contains the row and column indices of an empty cell.
        """
        return np.argwhere(self.map == 0)

    def get_winner(self):
        """
        This function checks if there is a winner in a game by checking the columns, rows, and
        diagonals.
        :return: a boolean value indicating whether there is a winner in the game board. If there is a
        winner, it returns True, otherwise it returns False (represented by 0 in this case).
        """
        is_winner_column = self.get_winner_column()
        is_winner_row = self.get_winner_row()
        is_winner_diagonal = self.get_winner_diagonal()

        return is_winner_column or is_winner_row or is_winner_diagonal or 0

    def get_winner_column(self):
        """
        This function checks the columns of a matrix to see if there is a winner and returns the winning
        symbol or 0 if there is no winner.
        :return: the symbol of the player who has won the game by filling a column of the game board. If
        no player has won by filling a column, the function returns 0.
        """
        for col in self.map.T:
            symbol = col[0]
            for row in col:
                if row != symbol:
                    symbol = None
                    break
            
            if symbol != None and symbol != 0:
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
            
            if symbol != None and symbol != 0:
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

        if symbol != None and symbol != 0:
            return symbol

        symbol = self.map[0, width - 1]
        for i in range(len(self.map) - 1):
            if  i < width and self.map[i, width - 1 - i] != symbol:
                symbol = None
                break

        if symbol != None and symbol != 0:
            return symbol

        return 0

    def is_game_over(self):
        """
        The function checks if the game is over by determining if the board is full or if there is a
        winner.
        :return: a boolean value indicating whether the game is over or not. It checks if the board is
        full or if there is a winner, and returns True if either condition is met, and False otherwise.
        """
        is_full = self.is_full()
        winner = self.get_winner()
        return is_full or winner != 0