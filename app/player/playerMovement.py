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


# Ensure the new position is within bounds
def ensure_bounds(player_pos: list[int], world_width: int, world_height: int) -> list[int]:
    if player_pos[0] < 0: player_pos[0] = 0
    if player_pos[0] >= world_height: player_pos[0] = world_height - 1
    if player_pos[1] < 0: player_pos[1] = 0
    if player_pos[1] >= world_width: player_pos[1] = world_width - 1

    return player_pos


# Change the player's position in the world
def update_player_position_to_world(old_player_pos: list[int], player_pos: list[int], world: list[list[str]]) -> list[list[str]]:
    world[old_player_pos[0]][old_player_pos[1]] = "  "
    world[player_pos[0]][player_pos[1]] = "x"

    return world


def moving(self, key: str, world: list[list[int]]):        
    old_pos = [self.pos[0], self.pos[1]]

    self.pos = change_player_position(key, self.pos)
    self.pos = ensure_bounds(self.pos, len(world), len(world[0]))

    world = update_player_position_to_world(old_pos, self.pos, world)
