from abc import ABC, abstractmethod

from app.utils import idGenerator


class Entity(ABC):
    id_generator = idGenerator.sequential_id_generator()

    @abstractmethod
    def __init__(self, hp: int, loot_table: list["item"], position: list[int]):
        self._id = next(Entity.id_generator)
        self.frame = 0
        self.position = position
        self.hp = hp
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
        for item in loot_table:
            #item.spawn
            pass
     

