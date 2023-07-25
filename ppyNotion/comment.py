'''
    `Comment` class in Notion page
'''
from typing import Dict, Optional
from .interface.i_notion_object import INotionObject
from .parent import Parent


class Comment(INotionObject):
    '''
    Comment object in Notion page

        Parameters:
            obj(dict) : 
    '''
    def __init__(self, obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj: Dict) -> None:
        self.id = obj.get('id')

        parent_value = obj.get('parent')
        if isinstance(parent_value, Parent) or parent_value is None:
            self.parent = parent_value
        else:
            self.set_parent(parent_value)

        self.discussion_id = obj.get('discussion_id')

        self.created_time = obj.get('created_time')

        self.last_edited_time = obj.get('last_edited_time')

        created_by_value = obj.get('created_by')
        if isinstance(created_by_value, User) or created_by_value is None:
            self.created_by = created_by_value
        else:
            self.set_created_by(created_by_value)

        rich_text_value = obj.get('rich_text')
        if isinstance(rich_text_value, RichText) or rich_text_value is None:
            self.rich_text = rich_text_value
        else:
            self.set_rich_text(rich_text_value)

    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def id(self) -> str:
        """
            return the id(str) in class
        """
        try:
            self.__id
        except AttributeError:
            self.__id = str()
        return self.__id

    @property
    def parent(self) -> Parent:
        """
            return the parent(Parent) in class
        """
        try:
            self.__parent
        except AttributeError:
            self.__parent = Parent()
        return self.__parent

    @property
    def discussion_id(self) -> str:
        """
            return the discussion_id(str) in class
        """
        try:
            self.__discussion_id
        except AttributeError:
            self.__discussion_id = str()
        return self.__discussion_id

    @property
    def created_time(self) -> datetime:
        """
            return the created_time(datetime) in class
        """
        try:
            self.__created_time
        except AttributeError:
            self.__created_time = datetime()
        return self.__created_time

    @property
    def last_edited_time(self) -> datetime:
        """
            return the last_edited_time(datetime) in class
        """
        try:
            self.__last_edited_time
        except AttributeError:
            self.__last_edited_time = datetime()
        return self.__last_edited_time

    @property
    def created_by(self) -> User:
        """
            return the created_by(User) in class
        """
        try:
            self.__created_by
        except AttributeError:
            self.__created_by = User()
        return self.__created_by

    @property
    def rich_text(self) -> RichText:
        """
            return the rich_text(RichText) in class
        """
        try:
            self.__rich_text
        except AttributeError:
            self.__rich_text = RichText()
        return self.__rich_text

    @id.setter
    def id(self, var: Optional[str]) -> None:
        """
            set value to id variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("id must be a `str` or `None` type")
        self.__id = var

    @parent.setter
    def parent(self, var: Optional[Parent]) -> None:
        """
            set value to parent variable, need to be `Parent` or `None` type
        """
        if not isinstance(var, Parent) and var is not None:
            raise TypeError("parent must be a `Parent` or `None` type")
        self.__parent = var

    def set_parent(self, parent_value: str) -> None:
        """
            set type by type name,
            type name must be in `Parent` class
        """
        raise NotImplementedError

    @discussion_id.setter
    def discussion_id(self, var: Optional[str]) -> None:
        """
            set value to discussion_id variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("discussion_id must be a `str` or `None` type")
        self.__discussion_id = var

    @created_time.setter
    def created_time(self, var: Optional[datetime]) -> None:
        """
            set value to created_time variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError("created_time must be a `datetime` or `None` type")
        self.__created_time = var

    @last_edited_time.setter
    def last_edited_time(self, var: Optional[datetime]) -> None:
        """
            set value to last_edited_time variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError(
                "last_edited_time must be a `datetime` or `None` type")
        self.__last_edited_time = var

    @created_by.setter
    def created_by(self, var: Optional[User]) -> None:
        """
            set value to created_by variable, need to be `User` or `None` type
        """
        if not isinstance(var, User) and var is not None:
            raise TypeError("created_by must be a `User` or `None` type")
        self.__created_by = var

    def set_created_by(self, created_by_value: str) -> None:
        """
            set type by type name,
            type name must be in `User` class
        """
        raise NotImplementedError

    @rich_text.setter
    def rich_text(self, var: Optional[RichText]) -> None:
        """
            set value to rich_text variable, need to be `RichText` or `None` type
        """
        if not isinstance(var, RichText) and var is not None:
            raise TypeError("rich_text must be a `RichText` or `None` type")
        self.__rich_text = var

    def set_rich_text(self, rich_text_value: str) -> None:
        """
            set type by type name,
            type name must be in `RichText` class
        """
        raise NotImplementedError
