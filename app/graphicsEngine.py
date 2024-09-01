def refresh(*args):
    for arg in args:
        arg.refresh()

def clear(*args):
    for arg in args:
        arg.clear()

def draw_world(stdscr, world: list[list[int]], player_pos: list):
    clear(stdscr)
    refresh(stdscr)

