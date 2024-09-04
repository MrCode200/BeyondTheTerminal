from abc import ABC, abstractmethod

from app import idGenerator

class Entity(ABC):
    id_generator = idGenerator.sequential_item_id_generator()

    @abstractmethod
    def __init__(self, hp: int):
        self._id = next(Entity.id_generator)
        self.hp = hp
        self.frame = 0
        self.position = [None, None]

    @abstractmethod
    def map_action_to_frame(self):
        pass

    @abstractmethod
    def movement(self):
        if self.frame >= self.speed:
            print("movingAction")

