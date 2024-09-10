"""
Utility Functions Module

This module contains utility functions for managing positions within world boundaries and generating sequential IDs.

**Functions**:
    - **ensure_bounds**: Ensures that a given position stays within the specified world dimensions.
    - **sequential_id_generator**: Generates sequential IDs starting from a specified value with a given step size.
"""
def ensure_bounds(pos: list[int], world_width: int, world_height: int) -> list[int]:
    '''
    Ensures a position stays within the bounds of the world dimensions by adjusting the x and y coordinates.

    :param pos: The current position [x, y].
    :param world_width: The width of the world.
    :param world_height: The height of the world.
    :return: The adjusted position within the world bounds.
    '''
    if pos[0] < 0: pos[0] = 0
    if pos[0] >= world_height: pos[0] = world_height - 1
    if pos[1] < 0: pos[1] = 0
    if pos[1] >= world_width: pos[1] = world_width - 1

    return pos


def sequential_id_generator(firstval=0, step=1) -> int:
    '''
    A generator function that yields sequential IDs starting from a specified value with a given step size.

    :param firstval: The starting value for the ID sequence. Default is 0.
    :param step: The step size to increment the ID by. Default is 1.
    '''
    x = firstval
    while 1:
        yield x
        x += step