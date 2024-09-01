from abc import ABC, abstractmethod


class item(ABC):
    @abstractmethod
    def __init__(self, ID :int, max_stack: int):
        self.ID = ID