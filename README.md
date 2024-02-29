
# Battleship Game

The Battleship game is a strategy type guessing game for two players. It's played on ruled grids (boards) on which each player's fleet of ships (including battleships) are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

## Features

- Command-line interface for easy interaction
- Customizable board size and number of ships
- Automated input from file for quick game setup
- Detailed output with game result summary

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/battleship-game.git
cd battleship-game
```

### Running the Game

Navigate to the `src` directory and run the game with Python:

```sh
cd src
python game.py
```

## Game Setup

The game reads initial setup from `src/inputs/game_input.txt`, which includes the board size, number of ships, ship positions, and player moves.

## Output

The game outputs the final board states and game result to `outputs/output.txt`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
