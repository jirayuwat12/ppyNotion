from .Interface.INotionObject import INotionObject
from .type import ColorType
from typing import Dict

class Annotation(INotionObject):

    def __init__(self, obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        if 'bold' in obj:
            self.bold = obj['bold']

        if 'italic' in obj:
            self.italic = obj['italic']
        
        if 'strikethrough' in obj:
            self.strikethrough = obj['strikethrough']
        
        if 'underline' in obj:
            self.underline = obj['underline']
        
        if 'code' in obj:
            self.code = obj['code']
        
        if 'color' in obj:
            self.color = obj['color']
        
    def to_object(self) -> Dict:
        '''
        return object of all field 
        for each one, if not set , return to false.
        '''
        ret = {
            'bold' : self.bold,
            'italic' : self.italic,
            'strikethrough' : self.strikethrough,
            'underline' : self.underline,
            'code' : self.code,
            'color' : self.color.name
        }
        return ret

    def __str__(self) -> str:
        return str(self.to_object())
    
    @property     
    def bold(self) -> bool:     
        """    
            return the __bold(bool) in class    
        """    
        try : self.__bold    
        except : self.__bold = False    
        return self.__bold    

    @property     
    def italic(self) -> bool:     
        """    
            return the __italic(bool) in class    
        """    
        try : self.__italic    
        except : self.__italic = False    
        return self.__italic    

    @property     
    def strikethrough(self) -> bool:     
        """    
            return the __strikethrough(bool) in class    
        """    
        try : self.__strikethrough    
        except : self.__strikethrough = False    
        return self.__strikethrough    

    @property     
    def underline(self) -> bool:     
        """    
            return the __underline(bool) in class    
        """    
        try : self.__underline    
        except : self.__underline = False    
        return self.__underline    

    @property     
    def code(self) -> bool:     
        """    
            return the __code(bool) in class    
        """    
        try : self.__code    
        except : self.__code = False    
        return self.__code    

    @property     
    def color(self) -> ColorType:     
        """    
            return the __color(ColorType) in class    
        """    
        try : self.__color    
        except : self.__color = ColorType.default    
        return self.__color    


    @bold.setter     
    def bold(self, var : bool) -> None:    
        """    
            set value to bold variable, need to be `bool` type    
        """    
        if not isinstance(var, bool):    
            raise TypeError(f"bold must be a `bool` type")    
        self.__bold = var    

    @italic.setter     
    def italic(self, var : bool) -> None:    
        """    
            set value to italic variable, need to be `bool` type    
        """    
        if not isinstance(var, bool):    
            raise TypeError(f"italic must be a `bool` type")    
        self.__italic = var    

    @strikethrough.setter     
    def strikethrough(self, var : bool) -> None:    
        """    
            set value to strikethrough variable, need to be `bool` type    
        """    
        if not isinstance(var, bool):    
            raise TypeError(f"strikethrough must be a `bool` type")    
        self.__strikethrough = var    

    @underline.setter     
    def underline(self, var : bool) -> None:    
        """    
            set value to underline variable, need to be `bool` type    
        """    
        if not isinstance(var, bool):    
            raise TypeError(f"underline must be a `bool` type")    
        self.__underline = var    

    @code.setter     
    def code(self, var : bool) -> None:    
        """    
            set value to code variable, need to be `bool` type    
        """    
        if not isinstance(var, bool):    
            raise TypeError(f"code must be a `bool` type")    
        self.__code = var    

    @color.setter     
    def color(self, var : ColorType) -> None:    
        """    
            set value to color variable, need to be `ColorType` type    
        """    
        if not isinstance(var, ColorType):    
            raise TypeError(f"color must be a `ColorType` type")    
        self.__color = var    


if __name__ == "__main__":
    a = Annotation()
    print(a)