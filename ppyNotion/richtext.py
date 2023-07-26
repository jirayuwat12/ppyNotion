
from typing import Dict, List, Optional
from .interface.i_notion_object import INotionObject
from .base_text import BaseText
from .text import Text
from .equation import Equation
from .mention import Mention

class RichText(INotionObject):
    CLASS_NAV = {
            'text' : Text,
            'equation' : Equation,
            'mention' : Mention
    }

    def __init__(self, texts : List = None) -> None:
        if texts is not None:
            self.from_object(texts)

    def from_object(self, obj : List) -> None:
        texts = obj
        for text in texts:
            if isinstance(text, BaseText):
                self.rich_text.append(text)
            else:
                self.rich_text.append(self.CLASS_NAV[text['type']](obj = text))

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
