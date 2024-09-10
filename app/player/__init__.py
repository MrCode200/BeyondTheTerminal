"""
Player Package

This package provides the player class and functions for the player class.

**Modules**:
    **player**: Contains the player class
        **Classes**
            - **Player**: Represents a player in the game.
    **playerMovement**: Contains functions for the movement of the player
        **Functions**:
            - **change_player_position**: Updates the player's position based on the key pressed and changes the player's character representation. Is used by move_player.
            - **move_player**: Manages player movement by updating position, ensuring it remains within boundaries, and updating the world representation.
    **playerEngine**: This module initializes and manages a list of player instances in the game.
        **Variables**:
            - **player_list**: A list containing instances of the `Player` class, representing players in the game.



**Attributes**:
    - **__author__**: The author of this package.
    - **__version__**: The current version of the package.
"""

__version__ = "0.1.0"
__author__ = "MrCode200", "Kian19955"

from .player import Player
from .playerMovement import move_player, change_player_position
from .playerEngine import player_list

__all__ = ["Player", "move_player", "change_player_position", "player_list"]