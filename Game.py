from Board import Board 
from InputPlayer import InputPlayer
from RandomPlayer import RandomPlayer
from Player import Player 

class Game:
    """
    A class to represent a Tic Tac Toe game.
    player1 The first player
    """
    def __init__(self, player1: Player, player2: Player, x=3, y=3) -> None:
        self.player1 = player1
        self.player2 = player2
        self.current_player = None

        self.board = Board(x,y)
        
    def run(self, print_board=True):
        """
        This function runs a game loop where players take turns making moves on a board until the game
        is over, and returns the winner.
        
        :param print_board: A boolean parameter that determines whether or not to print the game board
        after each move. If set to True, the board will be printed; if set to False, it will not be
        printed, defaults to True (optional)
        :return: the winner of the game.
        """
        while not self.board.is_game_over():            
            x, y = self.next_player().move(self.board)
            self.board.make_move(y, x, self.current_player)
            if print_board:
                print(f"{self.current_player.name} made move ({x}, {y})")
                print(self.board)
                print()

        return self.board.get_winner()

    def next_player(self) -> Player:
        """
        This function switches the current player between player1 and player2 and returns the new
        current player.
        :return: the current player after switching to the next player.
        """
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return self.current_player
        

if __name__ == "__main__":
    player1 = InputPlayer("InputPlayer 1", 1)
    player2 = RandomPlayer("RandomPlayer 2", 2)
    game = Game(player1, player2)
    winner = game.run()

    if winner == 0:
        print("It's a draw!")
    else:
        print(f"Player {winner} won the game!")