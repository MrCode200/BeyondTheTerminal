import curses

if not curses.can_change_color():
    raise RuntimeError("The terminal does not support custom colors.")


# Custom Colors
# NOTE: custom color IDs must range from 101 to 767
COLOR_GREY = 101
curses.init_color(COLOR_GREY, 500, 500, 500)


# Init colors
curses.init_pair(1, curses.COLOR_RED, COLOR_GREY)


# Create Color Constants to access
DAMAGE_CLR = curses.color_pair(1)