# Ensure the new position is within bounds
def ensure_bounds(pos: list[int], world_width: int, world_height: int) -> list[int]:
    if pos[0] < 0: pos[0] = 0
    if pos[0] >= world_height: pos[0] = world_height - 1
    if pos[1] < 0: pos[1] = 0
    if pos[1] >= world_width: pos[1] = world_width - 1

    return pos