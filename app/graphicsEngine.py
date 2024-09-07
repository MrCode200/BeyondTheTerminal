import time

#just for test
max_y = max_x = 0
half_y = half_x = 0

def init_graphicsEngine(stdscr):
    global max_y, max_x
    global half_y, half_x
    # Get terminal size
    max_y, max_x = stdscr.getmaxyx()
    max_x -= 1
    max_y -= 1

    # Calculate viewport dimensions
    half_y = max_y // 2
    half_x = max_x // 2


def refresh(*args):
    for arg in args:
        arg.refresh()


def clear(*args):
    for arg in args:
        arg.clear()


# Change the player's position in the world
def update_position_to_world(char: str, old_pos: list[int], new_pos: list[int], world: list[list[str]]):
    world[old_pos[0]][old_pos[1]] = " "
    world[new_pos[0]][new_pos[1]] = char


def draw_info(stdscr, pos):
    stdscr.addstr(1, 1, f"Pos : {pos}")
    refresh(stdscr)


def draw_world(stdscr, world: list[list[int]], player_pos: list):
    clear(stdscr)

    # Get the edge value relative to the player and check so it is not less than 0
    relative_zero = [max(player_pos[0] - half_y, 0), max(player_pos[1] - half_x, 0)]

    # -2 instead of -1 for padding one chr
    relative_max_y = relative_zero[0] + max_y if relative_zero[0] + max_y <= len(world)  else len(world)
    relative_max_x = relative_zero[1] + max_x if relative_zero[1] + max_x <= len(world[0])  else len(world[0])

    # Enumirate from world[relative (0,0) to relative (0,0) + max]
    for index_row, row in enumerate(world[relative_zero[0]: relative_max_y]):
        for index_char, char in enumerate(row[relative_zero[1] : relative_max_x]):
            stdscr.addch(index_row, index_char, char)

    refresh(stdscr)

