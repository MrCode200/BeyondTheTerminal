"""
fontsAndColor Package

This package provides the Different

**Modules**:
    **colors**: This module manages custom colors and color pairs for terminal output using the `curses` library. It initializes custom color settings and provides a global constant for a specific color pair.
        **functions**
            - **init_custom_colors**: Initializes custom color settings and creates color pairs.
    **fonts**: Contains all fonts used for entities, player, items, environmentalObjects...

**Attributes**:
    - **__author__**: The author of this package.
    - **__version__**: The current version of the package.
"""

__author__ = "MrCode200"
__version__ = "0.1.0"

from .colors import init_custom_colors
from .fonts import player_font

__all__ = ["init_custom_colors", "player_font"]