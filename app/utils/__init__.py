"""
Utilities Package

This package provides utility functions to manage world boundaries and generate unique sequential IDs for game entities.

**Functions**:
    - **sequential_id_generator**: A generator function that yields sequential IDs starting from a specified value with a given step size.
    - **ensure_bounds**: Ensures a position stays within the bounds of the world dimensions by adjusting the x and y coordinates.

**Attributes**:
    - **__author__**: The author of this package.
    - **__version__**: The current version of the package.
"""

__author__ = 'MrCode200'
__version__ = '0.1.0'

from .utils import sequential_id_generator
from .utils import ensure_bounds

__all__ = ["sequential_id_generator", "ensure_bounds"]