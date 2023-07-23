'''
To store link in Notion Object
'''
from typing import Dict, Optional
from .interface.i_notion_object import INotionObject

class Link(INotionObject):
    '''
    To store link in Notion Object
    obj can be `Dict` or `str`
    '''
    def __init__(self, obj = None) -> None:
        if isinstance(obj, Dict):
            self.from_object(obj)
        elif isinstance(obj, str):
            self.url = obj

    def from_object(self, obj : Dict) -> None:
        self.url = obj.get('url')


    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def url(self) -> str:
        """
            return the url(str) in class
        """
        try :
            self.__url
        except AttributeError:
            self.__url = str()
        return self.__url


    @url.setter
    def url(self, var : Optional[str]) -> None:
        """
            set value to url variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("url must be a `str` or `None` type")
        self.__url = var
