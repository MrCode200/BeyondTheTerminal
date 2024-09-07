import curses
from curses import init_color, init_pair,color_pair
from curses import COLOR_RED


# Custom Colors
# NOTE: custom color IDs must range from 101 to 767
COLOR_GREY: int = 101
init_color(COLOR_GREY, 500, 500, 500)


# Init colors
init_pair(1, COLOR_RED, COLOR_GREY)


# Create Color Constants to access
DAMAGE_CLR: "color_pair" = color_pair(1)