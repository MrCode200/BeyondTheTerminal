from app.utils import ensure_bounds
from app.graphicsEngine import update_position_to_world

from app.fontsAndColors import player_font

# Update player position based on key input
def change_player_position(obj: "player", key: str) -> list[int]:
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


def moving(obj, key: str, world: list[list[str]]):
    old_pos: list[int] = [obj.pos[0], obj.pos[1]]

    obj.pos: list[int] = change_player_position(obj, key)
    obj.pos: list[int] = ensure_bounds(obj.pos, len(world) - 1, len(world[0]) - 1)

    update_position_to_world(obj.char, old_pos, obj.pos, world)
