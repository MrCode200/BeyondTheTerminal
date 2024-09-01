def generateWorld(world_height: int, world_width: int):
    # Create empty world with height {world_height} and width {world_width}
    world = [[" " for _ in range(world_width)] for _ in range(world_height)]

    # Add some objects in the world
    world[5][10] = "o"
    world[10][20] = "x"

    return world

