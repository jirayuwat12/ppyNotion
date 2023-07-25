
from typing import Dict, List, Optional
from .interface.i_notion_object import INotionObject
from .base_text import BaseText

class RichText(INotionObject):

    def __init__(self, texts : List = None) -> None:
        

    def from_object(self, obj : Dict) -> None:
        rich_text_value = obj.get('rich_text')
        if isinstance(rich_text_value, List[BaseText]) or rich_text_value is None:
            self.rich_text = rich_text_value
        else:
            self.set_rich_text(rich_text_value)


    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def rich_text(self) -> List[BaseText]:
        """
            return the rich_text(List[BaseText]) in class
        """
        try :
            self.__rich_text
        except AttributeError:
            self.__rich_text = list()
        return self.__rich_text


    @rich_text.setter
    def rich_text(self, var : Optional[List[BaseText]]) -> None:
        """
            set value to rich_text variable, need to be `List[BaseText]` or `None` type
        """
        if not isinstance(var, List[BaseText]) and var is not None:
            raise TypeError("rich_text must be a `List[BaseText]` or `None` type")
        self.__rich_text = var

    def set_rich_text(self, rich_text_value : str) -> None:
        """
            set type by type name,
            type name must be in `List[BaseText]` class
        """
        raise NotImplementedError
