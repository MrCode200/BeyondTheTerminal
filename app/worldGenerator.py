def generateWorld(world_height: int, world_width: int):
    # Create empty world with height {world_height} and width {world_width}
    world = [[" " for _ in range(world_width)] for _ in range(world_height)]

    # Add some objects in the world
    world[5][10] = "o"
    world[80][10] = "o"
    world[50][90] = "o"
    world[50][50] = "x"

    return world

