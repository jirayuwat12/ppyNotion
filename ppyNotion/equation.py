'''
to store equation in Notion Object
'''
from typing import Dict, Optional
from .base_text import BaseText

class Equation(BaseText):
    '''
    to store equation in Notion Object
    '''
    def __init__(self, obj: Dict = None) -> None:
        super().__init__(obj)
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        super().from_object(obj)

        self.expression = obj.get('equation').get('expression')


    def to_object(self) -> Dict:
        obj = super().to_object()
        obj['equation'] = {
            'expression' : self.expression
        }
        return obj

    @property
    def expression(self) -> str:
        """
            return the expression(str) in class
        """
        try :
            self.__expression
        except AttributeError:
            self.__expression = str()
        return self.__expression


    @expression.setter
    def expression(self, var : Optional[str]) -> None:
        """
            set value to expression variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("expression must be a `str` or `None` type")
        self.__expression = var
        self.plain_text = var
