'''
`BaseText` is the base class for other Rich text class
'''

from typing import Dict, Optional
from .type import BaseTextType
from .annotation import Annotation
from .interface.i_notion_object import INotionObject


class BaseText(INotionObject):
    '''
    `BaseText` is the base class for other Rich text class
    '''

    def __init__(self, obj: Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        type_value = obj.get('type')
        if isinstance(type_value, BaseTextType) or type_value is None:
            self.type = type_value
        else:
            self.set_type(type_value)

        annotations_value = obj.get('annotations')
        if isinstance(annotations_value, Annotation) or annotations_value is None:
            self.annotations = annotations_value
        else:
            self.set_annotations(annotations_value)

        self.plain_text = obj.get('plain_text')

        self.href = obj.get('href')

    def to_object(self) -> Dict:
        obj = dict()

        if self.type is not None:
            obj['type'] = self.type.name

        if self.annotations is not None:
            obj['annotations'] = self.annotations.to_object()

        if self.plain_text is not None:
            obj['plain_text'] = self.plain_text

        if self.href is not None:
            obj['href'] = self.href

        return obj

    @property
    def type(self) -> BaseTextType:
        """
            return the type(BaseTextType) in class
        """
        try :
            self.__type
        except AttributeError:
            self.__type = None
        return self.__type

    @property
    def annotations(self) -> Annotation:
        """
            return the annotations(Annotation) in class
        """
        try :
            self.__annotations
        except AttributeError:
            self.__annotations = Annotation()
        return self.__annotations

    @property
    def plain_text(self) -> str:
        """
            return the plain_text(str) in class
        """
        try :
            self.__plain_text
        except AttributeError:
            self.__plain_text = str()
        return self.__plain_text

    @property
    def href(self) -> str:
        """
            return the href(str) in class
        """
        try :
            self.__href
        except AttributeError:
            self.__href = str()
        return self.__href


    @type.setter
    def type(self, var : Optional[BaseTextType]) -> None:
        """
            set value to type variable, need to be `BaseTextType` or `None` type
        """
        if not isinstance(var, BaseTextType) and var is not None:
            raise TypeError("type must be a `BaseTextType` or `None` type")
        self.__type = var

    def set_type(self, type_value : str) -> None:
        """
            set type by type name,
            type name must be in `BaseTextType` class
        """
        self.type = BaseTextType[type_value]

    @annotations.setter
    def annotations(self, var : Optional[Annotation]) -> None:
        """
            set value to annotations variable, need to be `Annotation` or `None` type
        """
        if not isinstance(var, Annotation) and var is not None:
            raise TypeError("annotations must be a `Annotation` or `None` type")
        self.__annotations = var

    def set_annotations(self, annotations_value : Dict) -> None:
        """
            set type by type name,
            type name must be in `Annotation` class
        """
        self.annotations = Annotation(annotations_value)

    @plain_text.setter
    def plain_text(self, var : Optional[str]) -> None:
        """
            set value to plain_text variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("plain_text must be a `str` or `None` type")
        self.__plain_text = var

    @href.setter
    def href(self, var : Optional[str]) -> None:
        """
            set value to href variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("href must be a `str` or `None` type")
        self.__href = var
