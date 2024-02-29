class GameBoard:
    def __init__(self, size):
        """
        Initializes the game board with a specified size.

        :param size: Integer, the size of the board (size x size).
        """
        self.size = size
        self.grid = [['_' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, position):
        """
        Places a ship at the specified position.

        :param position: A tuple (x, y) representing the ship's position.
        """
        x, y = position
        if self.is_valid_position(x, y):
            self.grid[x][y] = 'S'
            self.ships.append(position)
        else:
            print(f"Invalid position: ({x}, {y})")

    def is_valid_position(self, x, y):
        """
        Checks if a position is within the bounds of the board.

        :param x: X-coordinate of the position.
        :param y: Y-coordinate of the position.
        :return: True if the position is valid, False otherwise.
        """
        return 0 <= x < self.size and 0 <= y < self.size

    def receive_attack(self, position):
        """
        Processes an attack on the given position.

        :param position: A tuple (x, y) representing the attack's position.
        :return: True if a ship is hit, False otherwise.
        """
        x, y = position
        if self.grid[x][y] == 'S':
            self.grid[x][y] = 'X'  # Mark as hit
            return True
        elif self.grid[x][y] == '_':
            self.grid[x][y] = 'O'  # Mark as miss
        return False

    def display(self):
        """
        Displays the current state of the board.
        """
        for row in self.grid:
            print(' '.join(row))

    def remaining_ships(self):
        """
        Counts the number of ships that haven't been hit.

        :return: Integer, the number of remaining ships.
        """
        return sum(1 for x, y in self.ships if self.grid[x][y] == 'S')
