'''
text is a type of text in rich text
'''
from typing import Dict, Optional
from .base_text import BaseText
from .link import Link

class Text(BaseText):
    '''
    One type if text in rich text
    '''

    def __init__(self, obj: Dict = None) -> None:
        super().__init__(obj)
        if obj is not None:
            self.from_object(obj=obj)

    def from_object(self, obj: Dict) -> None:
        super().from_object(obj)

        self.content = obj['text'].get('content')

        link_value = obj['text'].get('link')
        if isinstance(link_value, Link) or link_value is None:
            self.link = link_value
        else:
            self.set_link(link_value)


    def to_object(self) -> Dict:
        obj = super().to_object()
        
        obj[self.type.name] = dict()

        if self.content is not None:
            obj[self.type.name]['content'] = self.content

        if self.link is not None:
            obj[self.type.name]['link'] = self.link.to_object()

        return obj

    @property
    def content(self) -> str:
        """
            return the content(str) in class
        """
        try :
            self.__content
        except AttributeError:
            self.__content = str()
        return self.__content

    @property
    def link(self) -> Link:
        """
            return the link(Link) in class
        """
        try :
            self.__link
        except AttributeError:
            self.__link = Link()
        return self.__link


    @content.setter
    def content(self, var : Optional[str]) -> None:
        """
            set value to content variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("content must be a `str` or `None` type")
        self.__content = var

    @link.setter
    def link(self, var : Optional[Link]) -> None:
        """
            set value to link variable, need to be `Link` or `None` type
        """
        if not isinstance(var, Link) and var is not None:
            raise TypeError("link must be a `Link` or `None` type")
        self.__link = var

    def set_link(self, link_value : str) -> None:
        """
            set type by type name,
            type name must be in `Link` class
        """
        self.link = Link(link_value)
