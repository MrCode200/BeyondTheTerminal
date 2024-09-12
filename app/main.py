"""
Main Game Loop Module

This module is responsible for initializing the game, managing the main loop, and handling player inputs and graphics updates. It integrates various components like graphics, world generation, player movement, and color management using the `curses` library.

**Functions**:
    - **init_proj**: Initializes the game’s curses settings, including terminal display and custom colors.
    - **check_key**: Handles user input, processing player movement and game exit.
    - **main**: The main game loop that continuously updates the game screen and processes player actions.
"""

import curses
import time
from curses import wrapper

from app.graphicsEngine import init_graphicsEngine, draw_world, draw_info
from app import worldGenerator as wG
from app.fontsAndColors import init_custom_colors
from app.player import player_list

from app.constants import FPS

world = wG.generateWorld()


def init_proj(stdscr: curses.window):
    """
    Initialize the game’s graphical environment using the curses library.

    - Configures terminal settings, disables the cursor, and enables non-blocking input.
    - Initializes custom colors and sets up the game’s graphics engine.

    :param stdscr: The standard screen object from the curses library, representing the terminal window.
    """
    # Initialize color features of curses
    curses.start_color()
    curses.use_default_colors()

    curses.curs_set(0)
    stdscr.nodelay(True)

    init_custom_colors()
    init_graphicsEngine(stdscr)


def check_key(stdscr: curses.window):
    """
    Handle user input by checking for key presses and processing player actions.

    - Moves the player based on the key pressed (e.g., "w", "a", "s", "d").
    - Exits the game if the "q" key is pressed.

    :param stdscr: The standard screen object from the curses library, representing the terminal window.
    """
    try:
        key = stdscr.getkey()
        player_list[0].check_key(key, world)

        # Break if q was hit
        if key == 'q':
            stdscr.clear()
            #doesnt exit
            exit()
    except:
        pass


def main(stdscr: curses.window):
    """
    The main game loop that continuously updates the screen.

    - Initializes the project environment, checks for key presses, and redraws the game world.
    - Runs indefinitely, rendering the player’s position and updating the game’s state until q is pressed.

    :param stdscr: The standard screen object from the curses library, representing the terminal window.
    """
    init_proj(stdscr)

    while True:
        check_key(stdscr)
        draw_world(stdscr, world, player_list[0].pos)
        draw_info(stdscr, player_list[0].pos)
        stdscr.refresh()
        time.sleep(FPS)


if __name__ == '__main__':
    wrapper(main)

