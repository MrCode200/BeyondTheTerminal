#            [y , x ]
player_pos = [50, 50]

def check_key(key: str, stdscr, world: list[list[int]]):
    global player_pos

    old_player_pos = [player_pos[0], player_pos[1]]

    # Update player position based on key input
    if "w" in key:
        player_pos[0] -= 1
    elif "s" in key:
        player_pos[0] += 1
    if "a" in key:
        player_pos[1] -= 1
    elif "d" in key:
        player_pos[1] += 1

    # Ensure the new position is within bounds
    max_y, max_x = len(world), len(world[0])
    if player_pos[0] < 0: player_pos[0] = 0
    if player_pos[0] >= max_y: player_pos[0] = max_y - 1
    if player_pos[1] < 0: player_pos[1] = 0
    if player_pos[1] >= max_x: player_pos[1] = max_x - 1

    world[old_player_pos[0]][old_player_pos[1]] = " "
    world[player_pos[0]][player_pos[1]] = "x"
