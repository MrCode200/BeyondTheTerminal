"""
Graphics Engine Module

This module handles the graphical representation of the game world, including viewport initialization, player position updates, and world rendering.

**Functions**:
    - **init_graphicsEngine**: Initializes the graphics engine by retrieving terminal size and calculating viewport dimensions.
    - **update_position_to_world**: Updates the player's or object's position in the game world.
    - **draw_info**: Displays the player's stats information on the screen.
    - **draw_world**: Renders the game world relative to the player's position, adjusting for viewport size.

**Variables**
    - **max_x**: Players screen length
    - **max_y**: Players screen height
    - **half_x**: Players screen length half
    - **half_y**: Players screen height half
"""
max_y = max_x = 0
half_y = half_x = 0

def init_graphicsEngine(stdscr):
    """
    Initialize the graphics engine by retrieving the terminal size and calculating the viewport dimensions based on the terminal size.

    :param stdscr: The standard screen object from the curses library.
    """

    global max_y, max_x
    global half_y, half_x
    # Get terminal size
    max_y, max_x = stdscr.getmaxyx()
    max_x -= 1
    max_y -= 1

    # Calculate viewport dimensions
    half_y = max_y // 2
    half_x = max_x // 2


# Change the player's position in the world
def update_position_to_world(char: str, old_pos: list[int], new_pos: list[int], world: list[list[str]]):
    """
    Change the position of objects in the world.

    :param char: The character representing the objects.
    :param old_pos: The old position of the objects as a list of two integers [y, x].
    :param new_pos: The new position of the objects as a list of two integers [y, x].
    :param world: The game world represented as a 2D list of strings.
    """
    world[old_pos[0]][old_pos[1]] = " "
    world[new_pos[0]][new_pos[1]] = char


def draw_info(stdscr, pos):
    """
    Draw the player's stasts information on the screen.

    :param stdscr: The standard screen object from the curses library.
    :param pos: The current position of the player as a list of two integers [y, x].
    """
    stdscr.addstr(1, 1, f"Pos : {pos}")


def draw_world(stdscr, world: list[list[int]], player_pos: list):
    """
    Draw the game world on the screen relative to the player's position.

    :param stdscr: The standard screen object from the curses library.
    :param world: The game world represented as a 2D list of integers.
    :param player_pos: The current position of the player as a list of two integers [y, x].
    """
    stdscr.clear()

    # Get the edge value relative to the player and check so it is not less than 0
    relative_zero = [max(player_pos[0] - half_y, 0), max(player_pos[1] - half_x, 0)]

    # -2 instead of -1 for padding one chr
    relative_max_y = relative_zero[0] + max_y if relative_zero[0] + max_y <= len(world)  else len(world)
    relative_max_x = relative_zero[1] + max_x if relative_zero[1] + max_x <= len(world[0])  else len(world[0])

    # Enumirate from world[relative (0,0) to relative (0,0) + max]
    for index_row, row in enumerate(world[relative_zero[0]: relative_max_y]):
        for index_char, char in enumerate(row[relative_zero[1] : relative_max_x]):
            stdscr.addch(index_row, index_char, char)
