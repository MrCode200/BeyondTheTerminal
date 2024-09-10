"""
Entity Package

This package provides the Different

**Modules**:
    **entityBase**: Contains the player class
        **Classes**
            - **Entity**: Abstract base class for all entities in the game.

**Attributes**:
    - **__author__**: The author of this package.
    - **__version__**: The current version of the package.
"""

__author__ = "MrCode200"
__version__ = "0.1.0"

from .entityBase import Entity
from .entitiesEngine import * #Is empty

__all__ = ["Entity"]