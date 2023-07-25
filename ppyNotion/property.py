
from typing import Dict, Optional
from .interface.i_notion_object import INotionObject
from .type import PropertyType

class Property(INotionObject):

    def __init__(self, obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        self.id = obj.get('id')

        type_value = obj.get('type')
        if isinstance(type_value, PropertyType) or type_value is None:
            self.type = type_value
        else:
            self.set_type(type_value)


    def to_object(self) -> Dict:
        obj = dict()

        if self.id is not None:
            obj['id'] = self.id

        if self.type is not None:
            obj['type'] = self.type.name

        return obj

    @property
    def id(self) -> str:
        """
            return the id(str) in class
        """
        try :
            self.__id
        except AttributeError:
            self.__id = str()
        return self.__id

    @property
    def type(self) -> PropertyType:
        """
            return the type(PropertyType) in class
        """
        try :
            self.__type
        except AttributeError:
            self.__type = None
        return self.__type


    @id.setter
    def id(self, var : Optional[str]) -> None:
        """
            set value to id variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("id must be a `str` or `None` type")
        self.__id = var

    @type.setter
    def type(self, var : Optional[PropertyType]) -> None:
        """
            set value to type variable, need to be `PropertyType` or `None` type
        """
        if not isinstance(var, PropertyType) and var is not None:
            raise TypeError("type must be a `PropertyType` or `None` type")
        self.__type = var

    def set_type(self, type_value : str) -> None:
        """
            set type by type name,
            type name must be in `PropertyType` class
        """
        self.__type = PropertyType[type_value]
