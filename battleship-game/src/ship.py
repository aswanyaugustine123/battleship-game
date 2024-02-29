class Ship:
    def __init__(self, position):
        """
        Initializes a new Ship instance.

        :param position: A tuple (x, y) representing the ship's position on the game board.
        """
        self.position = position
        self.hit = False  # Initially, the ship is not hit.

    def is_hit(self, attack_position):
        """
        Checks if the ship is hit by an attack.

        :param attack_position: A tuple (x, y) representing the attack's position.
        :return: True if the ship is hit, False otherwise.
        """
        if self.position == attack_position:
            self.hit = True
            return True
        return False

    def is_sunk(self):
        """
        Checks if the ship is sunk.

        :return: True if the ship is hit (sunk), False otherwise.
        """
        return self.hit

    def __repr__(self):
        """
        Returns a string representation of the Ship instance, useful for debugging.
        """
        return f"Ship(position={self.position}, hit={self.hit})"
