import unittest
from src.ship import Ship

class TestShip(unittest.TestCase):
    def setUp(self):
        """Set up a ship for testing."""
        self.ship = Ship((2, 3))  # Initialize a ship at position (2, 3)

    def test_ship_hit(self):
        """Test that a ship reports being hit correctly."""
        self.assertFalse(self.ship.hit, "Ship should not be hit initially.")
        hit = self.ship.is_hit((2, 3))
        self.assertTrue(hit, "Ship should report a hit.")
        self.assertTrue(self.ship.hit, "Ship's hit status should be True after being hit.")

    def test_ship_miss(self):
        """Test that a ship reports a miss correctly."""
        miss = self.ship.is_hit((1, 1))
        self.assertFalse(miss, "Ship should report a miss.")
        self.assertFalse(self.ship.hit, "Ship's hit status should remain False after a miss.")

    def test_is_sunk(self):
        """Test that a ship reports being sunk correctly."""
        self.assertFalse(self.ship.is_sunk(), "Ship should not be sunk initially.")
        self.ship.is_hit((2, 3))
        self.assertTrue(self.ship.is_sunk(), "Ship should be sunk after being hit.")

if __name__ == '__main__':
    unittest.main()
