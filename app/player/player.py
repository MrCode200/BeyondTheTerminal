"""
This module defines the `Player` class for representing players in the game.

The `Player` class includes attributes and methods for managing player state and
behavior, including handling movement and managing the player's inventory.

**Classes**:
    - **Player**: Represents a player in the game.

**Usage**:
To use the `Player` class, create an instance with the player's name, initial health points, inventory, and position. Use the `check_key` method to handle player movement based on key inputs.
"""

from app.utils import sequential_id_generator
from .playerMovement import move_player


class Player:
    """
   Represents a player in the game.

   :cvar id_generator: A generator for unique player IDs.
   :ivar _id: The unique ID of the instance.
   :ivar name: The name of the player.
   :ivar pos: The current position of the player in the world.
   :ivar char: The character representing the player in the game.
   :ivar hp: The health points of the player.
   :ivar inventory: The inventory of the player containing entities.
   """

    id_generator = sequential_id_generator()

    def __init__(self, player_name: str, starting_hp: int, starting_inventory: list["entity"],
                 starting_pos: list[int]) -> None:
        """
        Initilizes a new player instance

        :param player_name: The name of the player
        :param starting_hp: The starting health points of the player
        :param starting_inventory: The starting inventory of the player
        :param starting_pos: the starting position of the player
        """
        self._id = next(Player.id_generator)
        self.name = player_name
        self.pos = starting_pos
        self.char = "◓"
        self.hp = starting_hp
        self.inventory = starting_inventory

    @property
    def id(self) -> int:
        return self._id

    def check_key(self, key: str, world: list[list[str]]) -> None:
        """
        Handle player movement based on key inputs.

        :param key: The key pressed by the player.
        :param world: The graphical representation of the world.
        """
        if key in "awsd":
            move_player(self, key, world)
