"""
This module defines the abstract base class for all entities in the game.

This module defines abstract base classes entites.

**Classes**:
    - **Entity**: Abstract base class for all entities in the game.

**Usage**:
The `Entity` class is intended to be subclassed to create specific types of entities
with their own implementations of `map_action_to_frame`, `movement`, and `on_death`.
Subclasses should initialize the entity with specific attributes and behaviors.
"""
from abc import ABC, abstractmethod

from app.utils import sequential_id_generator


class Entity(ABC):
    """
    Abstract base class for all entities in the game.

    :cvar id_generator: A generator for producing unique IDs for each entity.

    :ivar _id: The unique identifier for the entity.
    :ivar age: The age of the entity.
    :ivar position: The position of the entity in the world [x, y].
    :ivar hp: The health points of the entity.
    :ivar loot_table: A dictionary containing items and their drop probabilities.

    Methods:
        - **id**: Returns the unique identifier of the entity.
        - **map_action_to_frame**: Abstract method to map actions to frames.
        - **movement**: Abstract method to define the entity's movement.
        - **on_death**: Abstract method to define actions upon the entity's death.
    """
    id_generator = sequential_id_generator()

    @abstractmethod
    def __init__(self, hp: int, loot_table: dict["item", float], position: list[int]):
        """
        Initializes a new entity with the given health points, loot table, and position.

        :param hp: The health points of the entity.
        :param loot_table: A dictionary containing items and their drop probabilities.
        :param position: The position of the entity in the world [x, y].
        """
        self._id = next(Entity.id_generator)
        self.frame = 0
        self.position = position
        self.hp = hp
        # Should contain the item from Item class and the probability of it dropping
        self.loot_table = loot_table

    @property
    def id(self):
        return self._id

    @abstractmethod
    def map_action_to_frame(self):
        """
        Abstract method to map actions to frames.
        This method should be implemented by subclasses to define how actions are mapped to frames.
        """
        pass

    @abstractmethod
    def movement(self):
        """
        Abstract method to define the entity's movement.
        This method should be implemented by subclasses to define the movement behavior of the entity.
        """
        pass

    @abstractmethod
    def on_death(self):
        """
        Abstract method to define actions upon the entity's death.
        This method can be used by subclasses to define what happens when the entity dies.
        """
        for item in self.loot_table:
            # item.spawn
            pass
