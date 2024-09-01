from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def __init__(self, ID :int, hp: int):
        self._id = ID
        self.hp = hp
        self.frame = 0

    @abstractmethod
    def map_action_to_frame(self):
        pass

    @abstractmethod
    def movement(self):
        if self.frame >= self.speed:
            print("movingAction")