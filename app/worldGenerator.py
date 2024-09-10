"""
World Generator Module

This module is responsible for generating the game world and managing randomization through a seed. It creates a 2D world map with environmental objects placed at specific coordinates.

**Functions**:
    - **set_seed**: Sets the seed for the random number generator to control the randomness in world generation.
    - **generateWorld**: Generates a 2D game world with given dimensions and places objects at predefined coordinates.
"""
import random

from app import environmentalObjects
from app import entities

def set_seed(seed: int):
    """
    Set the seed for the random number generator.

    :param seed: The seed value to initialize the random number generator.
    """
    random.seed(seed)

def generateWorld(world_height: int, world_width: int) -> list[list[str]]:
    """
    Generate a world with the specified height and width.

    :param world_height: The height of the world.
    :param world_width: The width of the world.
    :return: A 2D list representing the generated world with objects placed at specific coordinates.
    """
    # Create empty world with height {world_height} and width {world_width}
    world = [[" " for _ in range(world_width)] for _ in range(world_height)]

    # Add some objects in the world
    world[5][10] = "o"
    world[80][10] = "o"
    world[50][90] = "o"
    world[50][50] = "x"

    return world

