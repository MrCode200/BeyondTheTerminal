"""
This module defines abstract base classes for different types of items in the application.

**Classes**:
    - **Item**: Abstract base class for all items. Defines common attributes such as position and stack size, and provides a unique ID for each item instance.
    - **ConsumableItem**: Abstract base class for consumable items. Inherits from `Item` and may define additional behavior for items that can be consumed.
    - **CraftableItem**: Abstract base class for craftable items. Inherits from `Item` and may include attributes or methods related to crafting.
    - **Tool**: Abstract base class for tools. Inherits from `Item` and includes additional attributes such as durability.

**Attributes**:
    - **id_generator**: A generator for unique item IDs, imported from `app.utils`.

**Usage**:
    from app.items.itemTemplate import Item, ConsumableItem, CraftableItem, Tool

    class HealthPotion(ConsumableItem):
        def __init__(self, pos, stack_size):
            super().__init__(pos, stack_size)

        def on_consume(self):
            print("Health restored!")

    class Sword(Tool):
        def __init__(self, pos, durability, stack_size):
            super().__init__(pos, durability, stack_size)

        def on_use(self):
            print("Swinging the sword!")



**Attributes**:
    - **id_generator**: A generator for unique item IDs, imported from `app.utils`.

# Example:
    >>> potion = HealthPotion([0, 0], 1)
    >>> print(potion.id)
    1
    >>> sword = Sword([1, 1], 100, 1)
    >>> print(sword.id)
    2
    >>> sword.on_use()
    Swinging the sword!
"""

from abc import ABC, abstractmethod

from app.utils import sequential_id_generator


class Item(ABC):
    """
    Abstract base class for items

    :cvar id_generator: A generator for unique item IDs.
    :ivar _id: The unique id of the instance
    :ivar pos: Position of item in the world. If None, it is not in inventory or storage
    :ivar stack_size: The size of the stack for the item.
    """
    id_generator = sequential_id_generator()

    @abstractmethod
    def __init__(self, pos: list[int], stack_size: int):
        """
        Initialize the Item instance with a unique ID and a position in the world.

        :param pos: A list representing the position of the item in the world.
        :param stack_size: The size of the stack for the item.
        """
        self._id = next(Item.id_generator)
        self.pos = pos
        self.stack_size = stack_size

    @property
    def id(self):
        return self._id
    

class ConsumableItem(Item):
    """
    Abstract base class for items

    :cvar id_generator: A generator for unique item IDs.
    :ivar _id: The unique id of the instance
    :ivar pos: Position of item in the world. If None, it is not in inventory or storage
    :ivar stack_size: The size of the stack for the item.
    """
    def __init__(self, pos: list[int], stack_size: int):
        """
        Initialize the Item instance with a unique ID and a position in the world.

        :param pos: A list representing the position of the item in the world.
        :param stack_size: The size of the stack for the item.
        """
        super().__init__(pos, stack_size)

    @abstractmethod 
    def on_consume(self):
        """
        Perform actions when the consumable item is consumed.
        """
        pass


class CraftableItem(Item):
    """
    Abstract base class for items

    :cvar id_generator: A generator for unique item IDs.
    :ivar _id: The unique id of the instance
    :ivar pos: Position of item in the world. If None, it is not in inventory or storage
    :ivar stack_size: The size of the stack for the item.
    """
    def __init__(self, pos: list[int], stack_size: int):
        """
        Initialize the Item instance with a unique ID and a position in the world.

        :param pos: A list representing the position of the item in the world.
        :param stack_size: The size of the stack for the item.
        """
        super().__init__(pos, stack_size)


class Tool(Item):
    """
    Abstract base class for Tools

    :cvar id_generator: A generator for unique item IDs.
    :ivar _id: The unique id of the instance
    :ivar pos: Position of item in the world. If None, it is not in inventory or storage
    :ivar durability: Durability of Item till destroyed
    :ivar stack_size: The size of the stack for the item.
    """
    def __init__(self, pos: list[int], durability: int, stack_size: int):
        """
        Initialize the Item instance with a unique ID and a position in the world.

        :param pos: A list representing the position of the item in the world.
        :param stack_size: The size of the stack for the item.
        :param durability: Number of uses before Tool breaks.
        """
        super().__init__(pos, stack_size)
        self.durability = durability

    @abstractmethod 
    def on_use(self):
        """
        Perform actions when the consumable item is used.
        """
        pass
