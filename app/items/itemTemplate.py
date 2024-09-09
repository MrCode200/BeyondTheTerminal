from abc import ABC, abstractmethod

from app import idGenerator

class Item(ABC):
    id_generator = idGenerator.sequential_item_id_generator()

    @abstractmethod
    def __init__(self, pos: list[int]):
        self._id = next(Item.id_generator)
        self.pos = pos

    @property
    def id(self):
        return self._id
    

class ConsumableItem(Item):
    def __init__(self, pos: list[int]):
        super().__init__(pos)

    @abstractmethod 
    def on_use(self):
        pass


class CraftableItem(Item):
    def __init__(self, pos: list[int]):
        super().__init__(pos)


class Tool(Item):
    def __init__(self, pos: list[int]):
        super().__init__(pos)

    @abstractmethod 
    def on_use(self):
        pass
    