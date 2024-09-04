#             [y , x  ]
player_pos = [50, 50]

def check_key(key: str, stdscr, world: list[list[str]]) -> list[list[str]]:
    global player_pos

    if key in "awsd":
        old_player_pos = [player_pos[0], player_pos[1]]

        player_pos = change_player_position(key, player_pos)
        player_pos = ensure_bounds(player_pos, len(world), len(world[0]))

        world = update_player_position_to_world(old_player_pos, player_pos, world)

        return world


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
