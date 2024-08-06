# Snake Game

## Overview

Welcome to the Snake Game repository! This project features a classic Snake game built using Pygame. The game challenges players to navigate a snake around the screen to eat food, grow in length, and avoid collisions with the walls or itself. The game includes a scoring system, a pause feature, and increasing difficulty based on the player's score.

## Description

In this Snake game, you control a snake that moves around a grid to eat randomly placed food items. Each time the snake eats food, it grows longer, and the game speeds up. The objective is to achieve the highest score possible by consuming as much food as you can while avoiding collisions with the screen edges or the snake’s own body. The game also features a pause function that allows players to temporarily stop the game, and a game over screen that provides an option to restart the game by pressing space.

## Features

- **Classic Gameplay:** Navigate the snake to eat food and grow.
- **Score System:** Track your score as you eat food. The game speeds up as you score more points.
- **Pause Feature:** Pause the game by pressing the spacebar. Press it again to resume.
- **Game Over Screen:** Display a game over message and allow the player to restart the game by pressing space.
- **Dynamic Difficulty:** The game's speed increases as the score goes up.
- **Game Reset:** Restart the game after a game over to play again.

## How to Play

1. **Run the Script:**
   - Ensure Pygame is installed. You can install it using pip:
     ```sh
     pip install pygame
     ```
   - Save the Python code in a file named `snake_game.py`.
   - Open your terminal or command prompt.
   - Navigate to the directory where `snake_game.py` is saved.
   - Run the script with the following command:
     ```sh
     python snake_game.py
     ```

2. **Gameplay Instructions:**
   - Use the arrow keys to control the direction of the snake:
     - **Up Arrow:** Move Up
     - **Down Arrow:** Move Down
     - **Left Arrow:** Move Left
     - **Right Arrow:** Move Right
   - Press the **Spacebar** to pause the game. Press it again to resume.
   - Avoid colliding with the screen edges or the snake's own body.
   - The game ends if the snake hits the edge or itself. Press the spacebar to restart after the game over screen.

## Installation

To run the game on your local machine:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/harshithabannu/snake-game.git
    ```
2. **Navigate to the Project Directory:**
    ```sh
    cd snake-game
    ```
3. **Ensure you have Python and Pygame installed:**
    - Install Pygame if not already installed:
      ```sh
      pip install pygame
      ```
4. **Run the Game Script:**
    ```sh
    python snake_game.py
    ```

## Contributing

Contributions are welcome! If you want to enhance the game or add new features, please:

1. **Fork the repository.**
2. **Create a new branch:**
   ```sh
   git checkout -b feature-branch

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

