"""
Player Initialization Module

This module initializes and manages a list of player instances in the game.

**Variables**:
    - **player_list**: A list containing instances of the `Player` class, representing players in the game.

**Usage**:
    - Import the `Player` class and create instances as needed.
    - Initialize `player_list` with player instances, each having attributes such as name, health points, inventory, and position.
"""
from .player import Player

player_list = [Player("Magic", 100, [], [50, 50])]
