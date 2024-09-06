from abc import ABC, abstractmethode

from app import idGenerator
from app.player import playerMovement as pM

class player():
    id_generator = idGenerator.sequential_item_id_generator()

    def __init__(self, player_name: str, starting_hp: int, starting_inventory: list["entity"]):
        self._id = next(player.id_generator)
        self.name = player_name
        self.pos = [0, 0]
        self.hp = starting_hp
        self.inventory = starting_inventory

    @property
    def id(self):
        return self._id

    def check_key(self, key: str, stdscr, world: list[list[str]]) -> list[list[str]]:

        if key in "awsd":
            pM.moving(self, key)