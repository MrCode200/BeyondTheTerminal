"""
World Generator Module

This module is responsible for generating the game world and managing randomization through a seed. It creates a 2D world map with environmental objects placed at specific coordinates.

**Functions**:
    - **set_seed**: Sets the seed for the random number generator to control the randomness in world generation.
    - **generateWorld**: Generates a 2D game world with given dimensions and places objects at predefined coordinates.
"""
import random

import noise
import numpy as np

from app import environmentalObjects
from app import entities
from app.constants import WORLD_HEIGHT, WORLD_WIDTH, scale, octaves, persistence, lacunarity
##-----------------------test-------------------------------------------
terrain_probability_dict: {float | int, str} = {-1: "e", 0.2 : "o", 0.5 : "M", 1 : "#"}

def generate_terrain(world: list[list[str]]):
    keys = sorted(terrain_probability_dict.keys())
      # Sort the keys for proper range checking
    for y in range(len(world)):
        for x in range(len(world[0])):
            print(y, x)

            for i in range(1, len(keys)):
                if keys[i - 1] < world[y][x] <= keys[i]:
                    world[y][x] = terrain_probability_dict[keys[i]]


def generate_perlin_noise(world: list[list[str]], scale: int, octaves: int, persistence: int, lacunarity: int):
    """
    Generate a 2D Perlin noise-based terrain map.
    
    :param width: The width of the world.
    :param height: The height of the world.
    :param scale: The scale of the noise (higher values make the noise more "zoomed in").
    :param octaves: The number of layers of noise.
    :param persistence: Controls how much each octave contributes to the overall shape.
    :param lacunarity: Controls the frequency of octaves.
    :return: A 2D numpy array with normalized Perlin noise values between 0 and 1.
    """
    for y in range(len(world)):
        for x in range(len(world[0])):
            world[y][x] = noise.pnoise2(x/scale,  # x-coordinate (scaled)
                                          y/scale,  # y-coordinate (scaled)
                                          octaves=octaves,       # Level of detail
                                          persistence=persistence,  # How persistent details are
                                          lacunarity=lacunarity)  # Frequency of details

    #Find min and max values in the 2D array
    min_value = min(min(row) for row in world)
    max_value = max(max(row) for row in world)

    #Normalize the array
    for y in range(len(world)):
        for x in range(len(world[0])):
            world[y][x] = (world[y][x] - min_value) / (max_value - min_value)
##-------------------------------------------------------------------
def set_seed(seed: int):
    """
    Set the seed for the random number generator.

    :param seed: The seed value to initialize the random number generator.
    """
    random.seed(seed)


def generateWorld() -> list[list[str]]:
    """
    Generate a world with the specified height and width.

    :param world_height: The height of the world.
    :param world_width: The width of the world.
    :return: A 2D list representing the generated world with objects placed at specific coordinates.
    """
    # Create empty world with height {world_height} and width {world_width}
    world = [[" " for _ in range(WORLD_HEIGHT)] for _ in range(WORLD_WIDTH)]

    generate_perlin_noise(world=world, scale=scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
    generate_terrain(world=world)

    return world
