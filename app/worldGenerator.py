"""
World Generator Module

This module is responsible for generating the game world and managing randomization through a seed. It creates a 2D world map with environmental objects placed at specific coordinates.

**Functions**:
    - **set_seed**: Sets the seed for the random number generator to control the randomness in world generation.
    - **generateWorld**: Generates a 2D game world with given dimensions and places objects at predefined coordinates.
    - **generate_terrain**: Converts a 2D map of numeric values into a 2D map of terrain types based on predefined probability ranges.
    - **generate_perlin_noise**: Generates a 2D Perlin noise-based terrain map.
"""
import random

from noise import pnoise2

from app.constants import (WORLD_HEIGHT, WORLD_WIDTH,
                           terrain_probability_dict, scale, octaves, persistence, lacunarity,
                           world_seed)

def set_seed(seed: int):
    global world_seed
    """
    Set the seed for the random number generator.

    :param seed: The seed value to initialize the random number generator.
    """
    random.seed(seed)
    world_seed(seed)


def generate_perlin_noise(world: list[list[str]], scale: int, octaves: int, persistence: int, lacunarity: int, seed: int):
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
    print(len(world))
    for y in range(len(world)):
        for x in range(len(world[0])):
            world[y][x] = pnoise2(x/scale,  # x-coordinate (scaled)
                                          y/scale,  # y-coordinate (scaled)
                                          octaves=octaves,       # Level of detail
                                          persistence=persistence,  # How persistent details are
                                          lacunarity=lacunarity,
                                          base = seed)  # Frequency of details

    #Find min and max values in the 2D array
    min_value = min(min(row) for row in world)
    max_value = max(max(row) for row in world)

    #Normalize the array
    for y in range(len(world)):
        for x in range(len(world[0])):
            world[y][x] = (world[y][x] - min_value) / (max_value - min_value)


def generate_terrain(empty_world: list[list[int]]) -> list[list[str]]:
    """
    Converts a 2D map of numeric values into a 2D map of terrain types based on predefined probability ranges.

    :param empty_world: A 2D list of numeric values (floats or ints) representing the raw terrain data.
    :return: A 2D list of strings representing the terrain types where each cell is replaced by a terrain type from `terrain_probability_dict`.
    """
    new_world = [[" " for _ in range(WORLD_WIDTH)] for _ in range(WORLD_HEIGHT)]

    keys = sorted(terrain_probability_dict.keys())
   # Sort the keys for proper range checking
    for i in range(1, len(keys)):
        for y in range(len(empty_world)):
            for x in range(len(empty_world[0])):
                if keys[i - 1] < empty_world[y][x] <= keys[i]:
                    new_world[y][x] = terrain_probability_dict[keys[i]]

    return new_world


def generateWorld() -> list[list[str]]:
    """
    Generate a world with the specified height and width.

    :param world_height: The height of the world.
    :param world_width: The width of the world.
    :return: A 2D list representing the generated world with objects placed at specific coordinates.
    """
    # Create empty world with height {world_width} and width {world_height}
    world = [[" " for _ in range(WORLD_WIDTH)] for _ in range(WORLD_HEIGHT)]

    generate_perlin_noise(world=world, scale=scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
    world = generate_terrain(empty_world=world)

    return world
