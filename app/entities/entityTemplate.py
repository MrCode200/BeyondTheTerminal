from abc import ABC, abstractmethod

from app.utils import idGenerator


class Entity(ABC):
    id_generator = idGenerator.sequential_item_id_generator()

    @abstractmethod
    def __init__(self, hp: int, loot_table: dict["item", float], position: list[int]):
        self._id = next(Entity.id_generator)
        self.age = 0
        self.position = position
        self.hp = hp
        # Should contain the item from Item class and the probability of it dropping
        self.loot_table = loot_table

    @property
    def id(self):
        return self._id

    @abstractmethod
    def map_action_to_frame(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def on_death(self):
        for item in self.loot_table:
            # item.spawn
            pass
