from abc import ABC, abstractmethod

from app.utils import idGenerator


class Item(ABC):
    id_generator = idGenerator.sequential_id_generator()

    @abstractmethod
    def __init__(self, item_type :str = "item"):
        self._id = next(Item.id_generator)
        self.item_type = item_type

    @property
    def id(self):
        return self._id
