import curses
from curses import init_color, init_pair,color_pair
from curses import COLOR_RED

# Custom Color IDs
COLOR_GREY: int = 101

# Custom Color pair instance
DAMAGE_CLR = None

def init_custom_colors():
    global DAMAGE_CLR

    # Custom Colors
    # NOTE: custom color IDs must range from 101 to 767
    init_color(COLOR_GREY, 500, 500, 500)


    # Init colors
    init_pair(1, COLOR_RED, COLOR_GREY)


    # Create Color Constants to access
    DAMAGE_CLR = color_pair(1)

    