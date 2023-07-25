'''
    One kind of Property object
'''
from typing import Dict, Optional
from .property import Property

class Checkbox(Property):
    '''
    One kind of Property object

        Parameters:
            obj(dict) : object that like Notion API,
            check_status(bool) : if not pass obj or obj = `None`
                then use check_status to create class
    '''
    def __init__(self,
                 obj : Dict = None,
                 check_status : bool = None) -> None:

        super().__init__(obj = obj)

        if obj is not None:
            super().from_object(obj=obj)
            self.from_object(obj = obj)
        else:
            self.checkbox = check_status

    def from_object(self, obj : Dict) -> None:
        super().from_object(obj)

        self.checkbox = obj.get('checkbox')


    def to_object(self) -> Dict:
        obj = super().to_object()

        if self.checkbox is not None:
            obj['checkbox'] = self.checkbox

        return obj

    @property
    def checkbox(self) -> bool:
        """
            return the checkbox(bool) in class
        """
        try :
            self.__checkbox
        except AttributeError:
            self.__checkbox = bool()
        return self.__checkbox


    @checkbox.setter
    def checkbox(self, var : Optional[bool]) -> None:
        """
            set value to checkbox variable, need to be `bool` or `None` type
        """
        if not isinstance(var, bool) and var is not None:
            raise TypeError("checkbox must be a `bool` or `None` type")
        self.__checkbox = var

