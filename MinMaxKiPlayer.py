import math
import numpy as np
from Player import Player
from Board import Board
from typing import Tuple
from Game import Game

# The MinMaxKiPlayer class is a subclass of the Player class in Python.
class MinMaxKiPlayer(Player):
    def __init__(self, name, symbol, other_player = None) -> None:
        super().__init__(name, symbol)
        self.other_player = other_player

    def move(self, board: Board) -> Tuple[int, int]:
        """
        This function selects the best move for a player using the minimax algorithm with alpha-beta
        pruning.
        
        :param board: The current state of the game board
        :type board: Board
        :return: a tuple of two integers, representing the row and column of the best move on the board.
        """
        max_eval = -math.inf
        best_move = None
        moves = board.get_valid_moves()
        np.random.shuffle(moves)

        for move in moves:
            eval = self.minimax(move, 0, -math.inf, math.inf, False, board.copy(), self)
            print(f"Move: {move} Eval: {eval}")
            if eval > max_eval:
                max_eval = eval
                best_move = move

        return best_move[1], best_move[0]

    def evaluate(self, board: Board, depth):
        """
        This function evaluates the current state of a game board and returns a score based on the depth
        of the search and the winner of the game.
        
        :param board: The game board on which the evaluation is being performed
        :type board: Board
        :param depth: The depth parameter represents the current depth of the search in the game tree.
        It is used in the evaluation function to give a higher score to moves that lead to a win in
        fewer moves (i.e., at a lower depth)
        :return: a score based on the current state of the game board and the depth of the search. If
        the current player (represented by the symbol attribute of the class instance) has won, the
        function returns a high score based on the size of the board and the depth of the search. If the
        game is a tie, the function returns a lower score based on the size of the board
        """
        winner = board.get_winner()
        if winner == self.symbol:
            return (len(board) * len(board[0]))**2 - depth
        elif winner == 0:
            return (len(board) * len(board[0])) - depth
        else:
            return -1
  
    def max(self, board: Board, depth, alpha, beta):
        """
        This is a function that implements the max part of the minimax algorithm for a board game, with
        alpha-beta pruning.
        
        :param board: The current state of the game board
        :type board: Board
        :param depth: The current depth of the search tree. It is used to limit the depth of the search
        and prevent infinite recursion
        :param alpha: Alpha is the best value that the maximizing player (the player who is trying to
        maximize their score) has found so far in the current branch of the game tree. It is used to
        prune branches of the tree that are guaranteed to be worse than the current best option
        :param beta: Beta is the maximum value that the minimizing player (opponent) is willing to
        accept. It is used in the alpha-beta pruning algorithm to determine whether to continue
        evaluating a branch of the game tree or to prune it. If the maximum value found so far in a
        branch is greater than or equal to
        :return: the maximum evaluation value obtained by recursively calling the minimax function on
        all valid moves of the current board state.
        """
        max_eval = -math.inf

        for move in board.get_valid_moves():
            eval = self.minimax(move, depth + 1, alpha, beta, False, board.copy(), self)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval

    def min(self, board: Board, depth, alpha, beta):
        """
        This is a function that implements the minimax algorithm to find the minimum evaluation of a
        given board state at a certain depth, using alpha-beta pruning to optimize the search.
        
        :param board: The current state of the game board
        :type board: Board
        :param depth: The current depth of the search tree in the minimax algorithm. It starts at 0 and
        increases by 1 for each level of the tree that is explored
        :param alpha: Alpha is the best value that the maximizing player (in a minimax algorithm) has
        found so far at any level of the search tree. It represents the minimum score that the
        maximizing player is guaranteed to achieve
        :param beta: Beta is the maximum value that the minimizing player (in this case, the AI) is
        willing to accept. It is used in the alpha-beta pruning algorithm to eliminate branches of the
        game tree that are guaranteed to be worse than the current best option for the minimizing
        player. If the current evaluation of a
        :return: the minimum evaluation value obtained from the recursive minimax function calls.
        """
        min_eval = math.inf
  
        for move in board.get_valid_moves():
            eval = self.minimax(move, depth + 1, alpha, beta, True, board.copy(), self.other_player)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
    
        return min_eval

    def minimax(self, move, depth, alpha, beta, is_maximizing, board: Board, player: Player):
        """
        This is a minimax algorithm implementation for a two-player game with alpha-beta pruning.
        
        :param move: The move being considered by the minimax algorithm, represented as a tuple of (row,
        column) coordinates on the game board
        :param depth: The current depth of the search tree. It is used to limit the depth of the search
        and prevent the algorithm from exploring too many moves
        :param alpha: Alpha is the best value that the maximizing player currently has available. It is
        the lower bound of the possible values that the maximizing player can achieve
        :param beta: Beta is the minimum score that the minimizing player is guaranteed to achieve. It
        is used in the minimax algorithm to prune branches of the game tree that cannot lead to a better
        outcome for the minimizing player. If the current score of the maximizing player is greater than
        or equal to beta, then the minimizing
        :param is_maximizing: A boolean value indicating whether the current player is maximizing or
        minimizing their score. If it is True, then the current player is maximizing their score, and if
        it is False, then the current player is minimizing their score
        :param board: The current state of the game board
        :type board: Board
        :param player: The player parameter is an instance of the Player class, which represents the
        current player making the move
        :type player: Player
        :return: the result of either the `self.max()` or `self.min()` function, depending on the value
        of the `is_maximizing` parameter.
        """
        board.make_move(move[0], move[1], player)

        if board.is_game_over() or depth > len(board):
            return self.evaluate(board, depth)

        if is_maximizing:
            return self.max(board, depth, alpha, beta)
        
        return self.min(board, depth, alpha, beta)
            
if __name__ == "__main__":
    player1 = MinMaxKiPlayer("MinMaxKiPlayer 1", 1)
    player2 = MinMaxKiPlayer("MinMaxKiPlayer 2", 2, player1)
    player1.other_player = player2

    game = Game(player1, player2, x=3, y=3)
    winner = game.run()

    if winner == 0:
        print("It's a draw!")
    else:
        print(f"Player {winner} won the game!")