from .player import Player
from .gameboard import GameBoard

class Game:
    def __init__(self, size, ship_positions_p1, ship_positions_p2, moves_p1, moves_p2):
        self.board_size = size
        self.player1 = Player("Player 1", GameBoard(size, ship_positions_p1))
        self.player2 = Player("Player 2", GameBoard(size, ship_positions_p2))
        self.moves_p1 = moves_p1
        self.moves_p2 = moves_p2

    def start(self):
        """
        Starts the game, alternating turns between players until all moves are exhausted or all ships are sunk.
        """
        for move_p1, move_p2 in zip(self.moves_p1, self.moves_p2):
            print(f"{self.player1.name}'s turn")
            hit = self.player1.make_move(move_p1, self.player2.gameboard)
            self._print_result(hit, move_p1, self.player1.name)

            print(f"{self.player2.name}'s turn")
            hit = self.player2.make_move(move_p2, self.player1.gameboard)
            self._print_result(hit, move_p2, self.player2.name)

        self._determine_winner()

    def _print_result(self, hit, move, player_name):
        """
        Prints the result of a player's move.
        """
        result = "hit" if hit else "miss"
        print(f"{player_name} attacked {move} and it's a {result}!")

    def _determine_winner(self):
        """
        Determines the winner of the game based on the remaining ships.
        """
        ships_p1 = self.player1.gameboard.remaining_ships()
        ships_p2 = self.player2.gameboard.remaining_ships()

        print("Game Over")
        if ships_p1 > ships_p2:
            print(f"{self.player1.name} wins with {ships_p1} ships remaining!")
        elif ships_p2 > ships_p1:
            print(f"{self.player2.name} wins with {ships_p2} ships remaining!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    # Example initialization data
    size = 5  # Example board size
    ship_positions_p1 = [("1,1"), ("2,2"), ("3,3")]
    ship_positions_p2 = [("1,2"), ("2,3"), ("3,4")]
    moves_p1 = [("1,2"), ("2,3"), ("4,4")]
    moves_p2 = [("1,1"), ("3,3"), ("4,5")]

    game = Game(size, ship_positions_p1, ship_positions_p2, moves_p1, moves_p2)
    game.start()
