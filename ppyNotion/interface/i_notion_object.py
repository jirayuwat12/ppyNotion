'''
INotionObject class is a Interface class for most of class that use in Notion API
'''
from abc import ABC, abstractmethod
from typing import Dict


class INotionObject(ABC):
    '''
    There are 2 abstract method that need to implement.
    1. `from_object` : get object then set to class.
    2. `to_object` : convert all field in class into object.
    '''

    def __init__(self) -> None:
        pass

    @abstractmethod
    def from_object(self, obj: Dict) -> None:
        '''
        get object then set to class.

            Parameters:
                obj(Dict) : object from Notion API
        '''
        raise NotImplementedError

    @abstractmethod
    def to_object(self) -> Dict:
        '''
        return object from class's field

            Returns:
                object that use to send Notion API
        '''
        raise NotImplementedError
