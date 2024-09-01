from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def __init__(self, ID :int, item_type :str = "item"):
        self.ID = ID
        self.item_type = item_type