"""
This module contains the MinMaxKiPlayer class
"""

from typing import Tuple
import math
import numpy as np
from players.player import Player
from board import Board


class MinMaxKiPlayer(Player):
    """
    The MinMaxKiPlayer class is a subclass of the Player class in Python uses the minimax algorithm to find the best move
    """

    def __init__(self, name, symbol, other_player=None) -> None:
        super().__init__(name, symbol)
        self.other_player = other_player

    def move(self, board: Board) -> Tuple[int, int]:
        """
        This function selects the best move for a player using the minimax algorithm with alpha-beta
        pruning.
        """
        max_score = -math.inf
        best_move = None
        moves = board.get_valid_moves()
        np.random.shuffle(moves)

        for move in moves:
            score = self.minimax(move, 0, -math.inf,
                                 math.inf, False, board.copy(), self)
            print(f"Move: {move} Score: {score}")
            if score > max_score:
                max_score = score
                best_move = move

        return best_move[1], best_move[0]

    def evaluate(self, board: Board, depth):
        """
        This function evaluates the current state of a game board and returns a score based on the depth
        of the search and the winner of the game.
        """
        winner = board.get_winner()
        if winner == self.symbol:
            return (len(board) * len(board[0]))**2 - depth
        if winner == 0:
            return (len(board) * len(board[0])) - depth

        return -1

    def max(self, board: Board, depth, alpha, beta):
        """
        This is a function that implements the max part of the 
        minimax algorithm for a board game, with alpha-beta pruning.
        """
        max_score = -math.inf

        for move in board.get_valid_moves():
            score = self.minimax(move, depth + 1, alpha,
                                 beta, False, board.copy(), self)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return max_score

    def min(self, board: Board, depth, alpha, beta):
        """
        This is a function that implements the minimax algorithm to find the minimum evaluation of a
        given board state at a certain depth, using alpha-beta pruning to optimize the search.
        """
        min_score = math.inf

        for move in board.get_valid_moves():
            score = self.minimax(move, depth + 1, alpha,
                                 beta, True, board.copy(), self.other_player)
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break

        return min_score

    def minimax(self, move, depth, alpha, beta, is_maximizing, board: Board, player: Player):
        """
        This is a minimax algorithm implementation for a two-player game with alpha-beta pruning.
        """
        board.make_move(move[0], move[1], player)

        if board.is_game_over() or depth > len(board):
            return self.evaluate(board, depth)

        if is_maximizing:
            return self.max(board, depth, alpha, beta)

        return self.min(board, depth, alpha, beta)
