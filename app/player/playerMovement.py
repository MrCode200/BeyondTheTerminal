from app.utils import ensure_bounds
from app.graphicsEngine import update_position_to_world

# Update player position based on key input
def change_player_position(key: str, new_player_pos: list[int]) -> list[int]:
    if "w" in key:
        new_player_pos[0] -= 1
    elif "s" in key:
        new_player_pos[0] += 1
    if "a" in key:
        new_player_pos[1] -= 1
    elif "d" in key:
        new_player_pos[1] += 1

    return new_player_pos


def moving(obj, key: str, world: list[list[str]]):
    old_pos = [obj.pos[0], obj.pos[1]]

    obj.pos = change_player_position(key, obj.pos)
    obj.pos = ensure_bounds(obj.pos, len(world) - 1, len(world[0]) - 1)

    update_position_to_world(obj.char, old_pos, obj.pos, world)
