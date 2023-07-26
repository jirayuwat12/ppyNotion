from typing import Dict, Optional
from datetime import datetime
from .property import Property
from .utils.date_formatter import (
    datetime_to_iso8601,
    iso8601_to_datetime
)

class Date(Property):

    def __init__(self, obj: Dict = None) -> None:
        super().__init__(obj)
        if obj is not None:
            self.from_object(obj)


    def from_object(self, obj : Dict) -> None:
        super().from_object(obj = obj)

        start_var = obj.get('date').get('start')
        if isinstance(start_var, datetime) or start_var is None:
            self.start = obj.get('date').get('start')
        else:
            self.set_start(start_var)

        end_var = obj.get('date').get('end')
        if isinstance(end_var, datetime) or end_var is None:
            self.end = obj.get('date').get('end')
        else:
            self.set_end(end_var)

    def to_object(self) -> Dict:
        obj = super().to_object()

        obj['date'] = {
            'start' : datetime_to_iso8601(self.start)
        }
        if self.end is not None:
            obj['date']['end'] = datetime_to_iso8601(self.end)

        return obj

    @property
    def start(self) -> datetime:
        """
            return the start(datetime) in class
        """
        try :
            self.__start
        except AttributeError:
            self.__start = datetime()
        return self.__start

    @property
    def end(self) -> datetime:
        """
            return the end(datetime) in class
        """
        try :
            self.__end
        except AttributeError:
            self.__end = datetime()
        return self.__end


    @start.setter
    def start(self, var : Optional[datetime]) -> None:
        """
            set value to start variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError("start must be a `datetime` or `None` type")
        self.__start = var

    def set_start(self, start_str : str) -> None:
        '''
            set start field with iso8601 string
        '''
        if isinstance(start_str, str):
            self.__start = iso8601_to_datetime(start_str)

    def set_end(self, end_str : str) -> None:
        '''
            set end field with iso8601 string
        '''
        if isinstance(end_str, str):
            self.__end = iso8601_to_datetime(end_str)

    @end.setter
    def end(self, var : Optional[datetime]) -> None:
        """
            set value to end variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError("end must be a `datetime` or `None` type")
        self.__end = var
