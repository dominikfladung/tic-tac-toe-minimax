from Player import Player
from typing import Tuple
from Board import Board


# The class "InputPlayer" is a subclass of "Player" in Python.
class InputPlayer(Player):
    def move(self, board: Board) -> Tuple[int, int]:
        """
        This function prompts the user to enter coordinates for a move on a board and returns the
        coordinates if they are valid, otherwise it prints an error message and recursively calls
        itself.
        
        :param board: The board parameter is an instance of the Board class, which represents the game
        board on which the game is being played. It contains information about the current state of the
        board, such as the positions of the pieces and the status of each square (empty or occupied).
        The move() method takes this board
        :type board: Board
        :return: a tuple of two integers representing the coordinates (x, y) of a valid move on the
        board. If the move entered by the user is not valid, the function will print "Invalid move!" and
        call itself recursively until a valid move is entered.
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