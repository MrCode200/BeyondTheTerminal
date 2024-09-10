"""
Player Movement Module

This module handles player movement within the game world based on key inputs. It updates the player's position and graphical representation and ensures the player remains within world boundaries.

**Functions**:
    - **change_player_position**: Updates the player's position based on the key pressed and changes the player's character representation.
    - **move_player**: Manages player movement by updating position, ensuring it remains within boundaries, and updating the world representation.
"""
from app.utils import ensure_bounds
from app.graphicsEngine import update_position_to_world

from app.fontsAndColors import player_font


# Update player position based on key input
def change_player_position(obj: "player", key: str) -> list[int]:
    """Updates the player's position based on the key pressed and changes the player's character representation.

    :param obj: instance of type player
    :param key: gets key pressed
    :return: returns the new position of the player
    """
    new_player_pos: list[int] = obj.pos

    if "w" in key:
        new_player_pos[0] -= 1
        obj.char = player_font["up"]
    elif "s" in key:
        new_player_pos[0] += 1
        obj.char = player_font["down"]

    if "a" in key:
        new_player_pos[1] -= 1
        obj.char = player_font["left"]
    elif "d" in key:
        new_player_pos[1] += 1
        obj.char = player_font["right"]

    return new_player_pos


def move_player(obj, key: str, world: list[list[str]]) -> None:
    """

    :param obj: instance of type player
    :param key: key pressed
    :param world: the graphical representation of the world
    """
    old_pos: list[int] = [obj.pos[0], obj.pos[1]]

    obj.pos: list[int] = change_player_position(obj, key)
    obj.pos: list[int] = ensure_bounds(obj.pos, len(world) - 1, len(world[0]) - 1)

    print(old_pos, obj.pos)

    update_position_to_world(obj.char, old_pos, obj.pos, world)
