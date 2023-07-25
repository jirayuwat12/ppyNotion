
from typing import Dict, Optional
from .interface.i_notion_object import INotionObject
from .type import ColorType


class Choice(INotionObject):
    '''
    Choice class is use in property
    '''
    def __init__(self, obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)


    def from_object(self, obj : Dict) -> None:
        color_value = obj.get('color')
        if isinstance(color_value, ColorType) or color_value is None:
            self.color = color_value
        else:
            self.set_color(color_value)

        self.id = obj.get('id')

        self.name = obj.get('name')


    def to_object(self) -> Dict:
        obj = dict()

        if self.id is not None:
            obj['id'] = self.id

        if self.name is not None:
            obj['name'] = self.name

        if self.color is not None:
            obj['color'] = self.color.name

        return obj

    @property
    def color(self) -> ColorType:
        """
            return the color(ColorType) in class
        """
        try :
            self.__color
        except AttributeError:
            self.__color = ColorType["default"]
        return self.__color

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
    def name(self) -> str:
        """
            return the name(str) in class
        """
        try :
            self.__name
        except AttributeError:
            self.__name = str()
        return self.__name


    @color.setter
    def color(self, var : Optional[ColorType]) -> None:
        """
            set value to color variable, need to be `ColorType` or `None` type
        """
        if not isinstance(var, ColorType) and var is not None:
            raise TypeError("color must be a `ColorType` or `None` type")
        self.__color = var

    def set_color(self, color_value : str) -> None:
        """
            set type by type name,
            type name must be in `ColorType` class
        """
        self.__color = ColorType[color_value]

    @id.setter
    def id(self, var : Optional[str]) -> None:
        """
            set value to id variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("id must be a `str` or `None` type")
        self.__id = var

    @name.setter
    def name(self, var : Optional[str]) -> None:
        """
            set value to name variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("name must be a `str` or `None` type")
        self.__name = var
