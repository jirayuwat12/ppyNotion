from typing import Dict, Optional, Union
from .interface.i_notion_object import INotionObject

class Parent(INotionObject):

    def __init__(self, obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        self.type = obj.get('type')

        self.id = obj.get('id')


    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def type(self) -> str:
        """
            return the type(str) in class
        """
        try :
            self.__type
        except AttributeError:
            self.__type = str()
        return self.__type

    @property
    def id(self) -> Union[str, bool]:
        """
            return the id(Union[str, bool]) in class
        """
        try :
            self.__id
        except AttributeError:
            self.__id = Union[str, bool]()
        return self.__id


    @type.setter
    def type(self, var : Optional[str]) -> None:
        """
            set value to type variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("type must be a `str` or `None` type")
        self.__type = var

    @id.setter
    def id(self, var : Optional[Union[str, bool]]) -> None:
        """
            set value to id variable, need to be `Union[str, bool]` or `None` type
        """
        if not isinstance(var, Union[str, bool]) and var is not None:
            raise TypeError("id must be a `Union[str, bool]` or `None` type")
        self.__id = var

