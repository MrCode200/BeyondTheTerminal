from abc import ABC, abstractmethode

from app import idGenerator

class player(ABC):
    id_generator = idGenerator.sequential_item_id_generator()

    @abstractmethode 
    def __init__(self, starting_hp, starting_inventory):
        self._id = next(player.id_generator)
        self.hp = starting_hp
        self.inventory = starting_inventory

    @abstractmethode
    def moving():
        pass
