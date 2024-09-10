"""
Items Package

This package provides the Different

**Modules**:
    **itemBase**: Contains the player class
        **Classes**
            - **Item**: Abstract base class for all items. Defines common attributes such as position and stack size, and provides a unique ID for each item instance.
            - **ConsumableItem**: Abstract base class for consumable items. Inherits from `Item` and may define additional behavior for items that can be consumed.
            - **CraftableItem**: Abstract base class for craftable items. Inherits from `Item` and may include attributes or methods related to crafting.
            - **Tool**: Abstract base class for tools. Inherits from `Item` and includes additional attributes such as durability.

**Attributes**:
    - **__author__**: The author of this package.
    - **__version__**: The current version of the package.
"""
__author__ = "MrCode200"
__version__ = "0.1.0"

from .itemBase import Item, CraftableItem, ConsumableItem, Tool

__all__ = ["Item", "ConsumableItem", "CraftableItem", "Tool"]