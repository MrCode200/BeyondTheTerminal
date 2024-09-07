import time
import curses

from curses import wrapper

# Initialize global variables
# Constants
FPS = 1 / 60
WORLD_HEIGHT = 100
WORLD_WIDTH = 300

world = None
pE = None
gE = None


def init_project(stdscr: curses.window):
    global pE, gE, world
    # Initialize color features of curses
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)
    stdscr.nodelay(True)

    # Import modules after initializing curses
    import app.graphicsEngine as gE_module
    import app.player.playerEngine as pE_module
    import app.worldGenerator as wG_module

    # Initialize modules
    gE = gE_module
    pE = pE_module
    world = wG_module.generateWorld(WORLD_HEIGHT, WORLD_WIDTH)

    # Call initialization functions
    gE.init_graphicsEngine(stdscr)


def check_key(stdscr: curses.window):
    try:
        key = stdscr.getkey()
        pE.player_list[0].check_key(key, stdscr, world)
        # Break if 'q' was hit
        if key == 'q':
            gE.clear(stdscr)
            # Exit the program
            exit()
    except:
        pass


def main(stdscr: curses.window):
    print(1)
    init_project(stdscr)

    while True:
        check_key(stdscr)
        gE.draw_world(stdscr, world, pE.player_list[0].pos)
        gE.draw_info(stdscr, pE.player_list[0].pos)
        time.sleep(FPS)

# Run the curses application
wrapper(main)
