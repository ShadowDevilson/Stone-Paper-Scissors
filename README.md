# Rock-Paper-Scissors Game

This is a simple Rock-Paper-Scissors game implemented in Python. The game allows you to play against the computer, which randomly selects its choice. The game continues until you decide to exit.

## How to Play

1. **Run the Script**: Execute the `mainalt.py` script in your Python environment.
2. **Enter Your Choice**: When prompted, enter your choice among the following options:
   - `p` for Paper
   - `sc` for Scissors
   - `st` for Stone
3. **Exit the Game**: To exit the game, type `ex` when prompted for your choice.

## Game Rules

- **Stone (0)** beats **Scissors (-1)**
- **Scissors (-1)** beats **Paper (1)**
- **Paper (1)** beats **Stone (0)**

The game will display your choice, the computer's choice, and the result of the round (win, lose, or draw).

## Code Overview

The game logic is implemented in the `mainalt.py` file. Here's a brief overview of the code:

- The computer's choice is randomly selected from `[-1, 0, 1]`, representing Scissors, Stone, and Paper, respectively.
- The player's input is mapped to the corresponding values using a dictionary.
- The game compares the player's choice with the computer's choice and determines the result based on the rules of Rock-Paper-Scissors.
- The game continues in a loop until the player chooses to exit by typing `ex`.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `mainalt.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `mainalt.py` file.
4. Run the script using the following command:
   ```bash
   python mainalt.py


Example Output


Copy
Enter your choice among p, sc, st:
  p
You chose paper
Computer chose stone
You Win!   

Contributing:
shivamchak2000@gmail.com- Shivam Chakraborty.
