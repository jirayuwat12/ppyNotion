from abc import ABC, abstractmethod
from typing import Dict

class INotionObject(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def from_object(self, obj : Dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def to_object(self) -> Dict :
        raise NotImplementedError