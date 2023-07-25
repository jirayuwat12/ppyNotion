'''
to store emoji in Notion Object
'''
from typing import Dict, Optional, Any
from .interface.i_notion_object import INotionObject

class Emoji(INotionObject):
    '''
    to store emoji in Notion Object
    obj can be `emoji` or `object` from API

    '''

    def __init__(self, obj : Any = None) -> None:

        if isinstance(obj, Dict):
            self.from_object(obj)
        else:
            self.emoji = obj

    def from_object(self, obj : Dict) -> None:
        self.emoji = obj.get('emoji')


    def to_object(self) -> Dict:
        obj = dict()

        obj['type'] = 'emoji'
        obj['emoji'] = self.emoji

        return obj

    @property
    def emoji(self) -> str:
        """
            return the emoji(str) in class
        """
        try :
            self.__emoji
        except AttributeError:
            self.__emoji = str()
        return self.__emoji


    @emoji.setter
    def emoji(self, var : Optional[str]) -> None:
        """
            set value to emoji variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("emoji must be a `str` or `None` type")
        self.__emoji = var
