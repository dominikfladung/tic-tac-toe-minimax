"""
This is the main file of the game.
"""

from game import Game
from players.minimax_ki_player import MinMaxKiPlayer

player1 = MinMaxKiPlayer("MinMaxKiPlayer 1", 1)
player2 = MinMaxKiPlayer("MinMaxKiPlayer 2", 2, player1)
#    player1 = InputPlayer("InputPlayer 1", 1)
#    player2 = RandomPlayer("RandomPlayer 2", 2)
player1.other_player = player2

game = Game(player1, player2, x=4, y=4)
winner = game.run()

if winner == 0:
    print("It's a draw!")
else:
    print(f"Player {winner} won the game!")
