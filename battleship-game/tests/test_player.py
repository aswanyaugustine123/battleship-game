import unittest
from src.player import Player
from src.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test conditions for Player tests."""
        self.gameboard_p1 = GameBoard(5)  # Assuming a 5x5 board for Player 1
        self.gameboard_p2 = GameBoard(5)  # Assuming a 5x5 board for Player 2
        self.player1 = Player("Player 1", self.gameboard_p1)
        self.player2 = Player("Player 2", self.gameboard_p2)

        # Place ships for both players
        self.gameboard_p1.place_ship((1, 1))
        self.gameboard_p2.place_ship((2, 2))

    def test_make_move_hit(self):
        """Test making a move that results in a hit."""
        # Player 1 attacks Player 2's ship at (2, 2)
        hit = self.player1.make_move((2, 2), self.player2.gameboard)
        self.assertTrue(hit)
        # Check if Player 2's gameboard reflects the hit
        self.assertEqual(self.player2.gameboard.grid[2][2], 'X')

    def test_make_move_miss(self):
        """Test making a move that results in a miss."""
        # Player 1 attacks an empty position on Player 2's board
        miss = self.player1.make_move((0, 0), self.player2.gameboard)
        self.assertFalse(miss)
        # Check if Player 2's gameboard reflects the miss
        self.assertEqual(self.player2.gameboard.grid[0][0], 'O')

    def test_remaining_ships_after_hit(self):
        """Test the remaining ships count after a hit."""
        self.player1.make_move((2, 2), self.player2.gameboard)  # Player 1 hits Player 2's ship
        remaining_ships = self.player2.gameboard.remaining_ships()
        self.assertEqual(remaining_ships, 0)  # Assuming only 1 ship was placed

if __name__ == '__main__':
    unittest.main()
