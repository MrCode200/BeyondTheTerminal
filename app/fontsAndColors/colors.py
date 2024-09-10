"""
Color Management Module

This module manages custom colors and color pairs for terminal output using the `curses` library. It initializes custom color settings and provides a global constant for a specific color pair.

**Functions**:
    - **init_custom_colors**: Initializes custom color settings and creates color pairs.

**Usage**:
To add a new color, follow these steps:

1. **Define a Custom Color ID**:
    - Choose an integer ID between 101 and 767 for the custom color. E.g., `COLOR_BLUE = 102`.

2. **Initialize the Custom Color**:
    - Use `init_color(color_id, r, g, b)` where `color_id` is your chosen ID, and `r`, `g`, `b` are the RGB values (0-1000).
    - Example: `init_color(COLOR_BLUE, 0, 0, 1000)`

3. **Create a Color Pair**:
   - Use `init_pair(pair_number, foreground, background)` to define a color pair.
   - Example: `init_pair(2, COLOR_BLUE, COLOR_BLACK)`

4. **Access the Color Pair**:
   - Use `color_pair(pair_number)` to get the color pair constant.
   - Example: `MY_COLOR = color_pair(2)`
"""
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

    