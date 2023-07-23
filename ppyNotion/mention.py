from typing import Union, Dict, Optional
from .base_text import BaseText
from .database import Database
from .date import Date
from .link_preview import LinkPreview
from .page import Page
from .template_mention import TemplateMention
from .user import User
from .type import MentionType

class Mention(BaseText):
    '''
    for mention block in Notion object
    '''
    def __init__(self, obj: Dict = None) -> None:
        super().__init__(obj)
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        type_value = obj.get('type')
        if isinstance(type_value, MentionType) or type_value is None:
            self.type = type_value
        else:
            self.set_type(type_value)

        data_value = obj.get('data')
        if isinstance(data_value, 
                      Union[Database, Date, LinkPreview, Page, TemplateMention, User]) or data_value is None:
            self.data = data_value
        else:
            self.set_data(data_value)


    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def type(self) -> MentionType:
        """
            return the type(MentionType) in class
        """
        try :
            self.__type
        except AttributeError:
            self.__type = MentionType["default"]
        return self.__type

    @property
    def data(self) -> Union[Database, Date, LinkPreview, Page, TemplateMention, User]:
        """
            return the data(Union[Database, Date, LinkPreview, Page, TemplateMention, User]) in class
        """
        try :
            self.__data
        except AttributeError:
            self.__data = Union[Database, Date, LinkPreview, Page, TemplateMention, User]()
        return self.__data


    @type.setter
    def type(self, var : Optional[MentionType]) -> None:
        """
            set value to type variable, need to be `MentionType` or `None` type
        """
        if not isinstance(var, MentionType) and var is not None:
            raise TypeError("type must be a `MentionType` or `None` type")
        self.__type = var

    def set_type(self, type_value : str) -> None:
        """
            set type by type name,
            type name must be in `MentionType` class
        """
        raise NotImplementedError

    @data.setter
    def data(self, var : Optional[Union[Database, Date, LinkPreview, Page, TemplateMention, User]]) -> None:
        """
            set value to data variable, need to be `Union[Database, Date, LinkPreview, Page, TemplateMention, User]` or `None` type
        """
        if not isinstance(var, Union[Database, Date, LinkPreview, Page, TemplateMention, User]) and var is not None:
            raise TypeError("data must be a `Union[Database, Date, LinkPreview, Page, TemplateMention, User]` or `None` type")
        self.__data = var

    def set_data(self, data_value : str) -> None:
        """
            set type by type name,
            type name must be in `Union[Database, Date, LinkPreview, Page, TemplateMention, User]` class
        """
        raise NotImplementedError

