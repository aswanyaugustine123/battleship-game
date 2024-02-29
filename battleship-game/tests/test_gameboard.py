import unittest
from src.gameboard import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        """Set up a game board for each test."""
        self.gameboard = GameBoard(5)  # Create a 5x5 board

    def test_initialization(self):
        """Test board initialization."""
        self.assertEqual(len(self.gameboard.grid), 5)
        for row in self.gameboard.grid:
            self.assertEqual(len(row), 5)
            for cell in row:
                self.assertEqual(cell, '_')

    def test_place_ship_valid(self):
        """Test placing a ship at a valid position."""
        self.gameboard.place_ship((1, 1))
        self.assertEqual(self.gameboard.grid[1][1], 'S')

    def test_place_ship_invalid(self):
        """Test placing a ship at an invalid position."""
        with self.assertRaises(ValueError):  # Assuming you raise ValueError for invalid positions
            self.gameboard.place_ship((-1, -1))

    def test_receive_attack_hit(self):
        """Test receiving an attack that hits a ship."""
        self.gameboard.place_ship((2, 2))
        hit = self.gameboard.receive_attack((2, 2))
        self.assertTrue(hit)
        self.assertEqual(self.gameboard.grid[2][2], 'X')

    def test_receive_attack_miss(self):
        """Test receiving an attack that misses."""
        miss = self.gameboard.receive_attack((0, 0))
        self.assertFalse(miss)
        self.assertEqual(self.gameboard.grid[0][0], 'O')

    def test_remaining_ships(self):
        """Test counting remaining ships."""
        self.gameboard.place_ship((1, 1))
        self.gameboard.place_ship((2, 2))
        self.gameboard.receive_attack((1, 1))  # Hit one ship
        self.assertEqual(self.gameboard.remaining_ships(), 1)

if __name__ == '__main__':
    unittest.main()
