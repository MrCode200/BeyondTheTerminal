from abc import ABC, abstractmethod


class entity(ABC):
    @abstractmethod
    def __init__(self, ID :int, hp: int):
        self.ID = ID
        self.hp = hp