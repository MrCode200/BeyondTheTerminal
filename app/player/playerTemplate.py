from app.utils.idGenerator import sequential_id_generator
from app.player.playerMovement import moving

class player:
    id_generator = sequential_id_generator()

    def __init__(self, player_name: str, starting_hp: int, starting_inventory: list["entity"], starting_pos: list[int]):
        self._id = next(player.id_generator)
        self.name = player_name
        self.pos = starting_pos
        self.char = "◓"
        self.hp = starting_hp
        self.inventory = starting_inventory

    @property
    def id(self):
        return self._id

    def check_key(self, key: str, stdscr, world: list[list[str]]):

        if key in "awsd":
            moving(self, key, world)