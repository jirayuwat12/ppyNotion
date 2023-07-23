'''
Annotation class is use for Rich text object in Notion 
'''

from typing import Dict, Optional
from .interface.i_notion_object import INotionObject
from .type import ColorType


class Annotation(INotionObject):
    '''
    Annotation class is use for Rich text object in Notion 
    '''

    def __init__(self, obj: Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj: Dict) -> None:
        bold_var = obj.get('bold')
        self.bold = bold_var

        if 'italic' in obj:
            self.italic = obj['italic']

        if 'strikethrough' in obj:
            self.strikethrough = obj['strikethrough']

        if 'underline' in obj:
            self.underline = obj['underline']

        if 'code' in obj:
            self.code = obj['code']

        color_var = obj.get('color')
        if isinstance(color_var, ColorType) or color_var is None:
            self.color = color_var
        else:
            self.set_color(color_var)

    def to_object(self) -> Dict:
        '''
        return object of all field 
        for each one, if not set , return to false.
        '''
        ret = {
            'bold': self.bold,
            'italic': self.italic,
            'strikethrough': self.strikethrough,
            'underline': self.underline,
            'code': self.code,
            'color': self.color.name
        }
        return ret

    def __str__(self) -> str:
        return str(self.to_object())

    @property
    def bold(self) -> bool:
        """    
            return the __bold(bool) in class    
        """
        try:
            self.__bold
        except AttributeError:
            self.__bold = False
        return self.__bold

    @property
    def italic(self) -> bool:
        """    
            return the __italic(bool) in class    
        """
        try:
            self.__italic
        except AttributeError:
            self.__italic = False
        return self.__italic

    @property
    def strikethrough(self) -> bool:
        """    
            return the __strikethrough(bool) in class    
        """
        try:
            self.__strikethrough
        except AttributeError:
            self.__strikethrough = False
        return self.__strikethrough

    @property
    def underline(self) -> bool:
        """    
            return the __underline(bool) in class    
        """
        try:
            self.__underline
        except AttributeError:
            self.__underline = False
        return self.__underline

    @property
    def code(self) -> bool:
        """    
            return the __code(bool) in class    
        """
        try:
            self.__code
        except AttributeError:
            self.__code = False
        return self.__code

    @property
    def color(self) -> ColorType:
        """    
            return the __color(ColorType) in class    
        """
        try:
            self.__color
        except AttributeError:
            self.__color = ColorType.default
        return self.__color

    @bold.setter
    def bold(self, var: bool) -> None:
        """    
            set value to bold variable, need to be `bool` type    
        """
        if not isinstance(var, bool):
            raise TypeError("bold must be a `bool` type")
        self.__bold = var

    @italic.setter
    def italic(self, var: bool) -> None:
        """    
            set value to italic variable, need to be `bool` type    
        """
        if not isinstance(var, bool):
            raise TypeError("italic must be a `bool` type")
        self.__italic = var

    @strikethrough.setter
    def strikethrough(self, var: bool) -> None:
        """    
            set value to strikethrough variable, need to be `bool` type    
        """
        if not isinstance(var, bool):
            raise TypeError("strikethrough must be a `bool` type")
        self.__strikethrough = var

    @underline.setter
    def underline(self, var: bool) -> None:
        """    
            set value to underline variable, need to be `bool` type    
        """
        if not isinstance(var, bool):
            raise TypeError("underline must be a `bool` type")
        self.__underline = var

    @code.setter
    def code(self, var: bool) -> None:
        """    
            set value to code variable, need to be `bool` type    
        """
        if not isinstance(var, bool):
            raise TypeError("code must be a `bool` type")
        self.__code = var

    @color.setter
    def color(self, var: Optional[ColorType]) -> None:
        """    
            set value to color variable, need to be `ColorType` type    
        """
        if isinstance(var, ColorType) or var is None:
            self.__color = var
        else:
            raise TypeError("color must be a `ColorType` type\nor if you want to change by type name please use `set_color` instead")
    
    def set_color(self, color_type : str):
        if not isinstance(color_type, str):
            raise TypeError('must be `str` type ')
        self.__color = ColorType[color_type]