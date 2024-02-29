from .gameboard import GameBoard

class Player:
    def __init__(self, name, gameboard):
        """
        Initializes a new player with a name and a gameboard.

        :param name: The name of the player.
        :param gameboard: An instance of GameBoard representing the player's gameboard.
        """
        self.name = name
        self.gameboard = gameboard

    def make_move(self, move, opponent_board):
        """
        Attempts to hit a ship on the opponent's board with the given move.

        :param move: A tuple (x, y) representing the move coordinates.
        :param opponent_board: An instance of GameBoard representing the opponent's gameboard.
        :return: True if a ship is hit, False otherwise.
        """
        return opponent_board.receive_attack(move)

    def __str__(self):
        """
        Returns a string representation of the player.
        """
        return f"Player(name={self.name})"

