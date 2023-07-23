from typing import Dict, Optional
from datetime import datetime
from .user import User
from .file import File
from .parent import Parent
from .interface.i_notion_object import INotionObject

class Page(INotionObject):

    def __init__(self,obj : Dict = None) -> None:
        if obj is not None:
            self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        self.id = obj.get('id')

        self.created_time = obj.get('created_time')

        created_by_value = obj.get('created_by')
        if isinstance(created_by_value, User) or created_by_value is None:
            self.created_by = created_by_value
        else:
            self.set_created_by(created_by_value)

        self.last_edited_time = obj.get('last_edited_time')

        last_edited_by_value = obj.get('last_edited_by')
        if isinstance(last_edited_by_value, User) or last_edited_by_value is None:
            self.last_edited_by = last_edited_by_value
        else:
            self.set_last_edited_by(last_edited_by_value)

        self.archived = obj.get('archived')

        icon_value = obj.get('icon')
        if isinstance(icon_value, File) or icon_value is None:
            self.icon = icon_value
        else:
            self.set_icon(icon_value)

        cover_value = obj.get('cover')
        if isinstance(cover_value, File) or cover_value is None:
            self.cover = cover_value
        else:
            self.set_cover(cover_value)

        self.properties = obj.get('properties')

        parent_value = obj.get('parent')
        if isinstance(parent_value, Parent) or parent_value is None:
            self.parent = parent_value
        else:
            self.set_parent(parent_value)

        self.url = obj.get('url')

        self.public_url = obj.get('public_url')


    def to_object(self) -> Dict:
        obj = dict()

        return obj

    @property
    def id(self) -> str:
        """
            return the id(str) in class
        """
        try :
            self.__id
        except AttributeError:
            self.__id = str()
        return self.__id

    @property
    def created_time(self) -> datetime:
        """
            return the created_time(datetime) in class
        """
        try :
            self.__created_time
        except AttributeError:
            self.__created_time = datetime()
        return self.__created_time

    @property
    def created_by(self) -> User:
        """
            return the created_by(User) in class
        """
        try :
            self.__created_by
        except AttributeError:
            self.__created_by = User()
        return self.__created_by

    @property
    def last_edited_time(self) -> datetime:
        """
            return the last_edited_time(datetime) in class
        """
        try :
            self.__last_edited_time
        except AttributeError:
            self.__last_edited_time = datetime()
        return self.__last_edited_time

    @property
    def last_edited_by(self) -> User:
        """
            return the last_edited_by(User) in class
        """
        try :
            self.__last_edited_by
        except AttributeError:
            self.__last_edited_by = User()
        return self.__last_edited_by

    @property
    def archived(self) -> bool:
        """
            return the archived(bool) in class
        """
        try :
            self.__archived
        except AttributeError:
            self.__archived = bool()
        return self.__archived

    @property
    def icon(self) -> File:
        """
            return the icon(File) in class
        """
        try :
            self.__icon
        except AttributeError:
            self.__icon = File()
        return self.__icon

    @property
    def cover(self) -> File:
        """
            return the cover(File) in class
        """
        try :
            self.__cover
        except AttributeError:
            self.__cover = File()
        return self.__cover

    @property
    def properties(self) -> dict:
        """
            return the properties(dict) in class
        """
        try :
            self.__properties
        except AttributeError:
            self.__properties = dict()
        return self.__properties

    @property
    def parent(self) -> Parent:
        """
            return the parent(Parent) in class
        """
        try :
            self.__parent
        except AttributeError:
            self.__parent = Parent()
        return self.__parent

    @property
    def url(self) -> str:
        """
            return the url(str) in class
        """
        try :
            self.__url
        except AttributeError:
            self.__url = str()
        return self.__url

    @property
    def public_url(self) -> str:
        """
            return the public_url(str) in class
        """
        try :
            self.__public_url
        except AttributeError:
            self.__public_url = str()
        return self.__public_url


    @id.setter
    def id(self, var : Optional[str]) -> None:
        """
            set value to id variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("id must be a `str` or `None` type")
        self.__id = var

    @created_time.setter
    def created_time(self, var : Optional[datetime]) -> None:
        """
            set value to created_time variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError("created_time must be a `datetime` or `None` type")
        self.__created_time = var

    @created_by.setter
    def created_by(self, var : Optional[User]) -> None:
        """
            set value to created_by variable, need to be `User` or `None` type
        """
        if not isinstance(var, User) and var is not None:
            raise TypeError("created_by must be a `User` or `None` type")
        self.__created_by = var

    def set_created_by(self, created_by_value : str) -> None:
        """
            set type by type name,
            type name must be in `User` class
        """
        raise NotImplementedError

    @last_edited_time.setter
    def last_edited_time(self, var : Optional[datetime]) -> None:
        """
            set value to last_edited_time variable, need to be `datetime` or `None` type
        """
        if not isinstance(var, datetime) and var is not None:
            raise TypeError("last_edited_time must be a `datetime` or `None` type")
        self.__last_edited_time = var

    @last_edited_by.setter
    def last_edited_by(self, var : Optional[User]) -> None:
        """
            set value to last_edited_by variable, need to be `User` or `None` type
        """
        if not isinstance(var, User) and var is not None:
            raise TypeError("last_edited_by must be a `User` or `None` type")
        self.__last_edited_by = var

    def set_last_edited_by(self, last_edited_by_value : str) -> None:
        """
            set type by type name,
            type name must be in `User` class
        """
        raise NotImplementedError

    @archived.setter
    def archived(self, var : Optional[bool]) -> None:
        """
            set value to archived variable, need to be `bool` or `None` type
        """
        if not isinstance(var, bool) and var is not None:
            raise TypeError("archived must be a `bool` or `None` type")
        self.__archived = var

    @icon.setter
    def icon(self, var : Optional[File]) -> None:
        """
            set value to icon variable, need to be `File` or `None` type
        """
        if not isinstance(var, File) and var is not None:
            raise TypeError("icon must be a `File` or `None` type")
        self.__icon = var

    def set_icon(self, icon_value : str) -> None:
        """
            set type by type name,
            type name must be in `File` class
        """
        raise NotImplementedError

    @cover.setter
    def cover(self, var : Optional[File]) -> None:
        """
            set value to cover variable, need to be `File` or `None` type
        """
        if not isinstance(var, File) and var is not None:
            raise TypeError("cover must be a `File` or `None` type")
        self.__cover = var

    def set_cover(self, cover_value : str) -> None:
        """
            set type by type name,
            type name must be in `File` class
        """
        raise NotImplementedError

    @properties.setter
    def properties(self, var : Optional[dict]) -> None:
        """
            set value to properties variable, need to be `dict` or `None` type
        """
        if not isinstance(var, dict) and var is not None:
            raise TypeError("properties must be a `dict` or `None` type")
        self.__properties = var

    @parent.setter
    def parent(self, var : Optional[Parent]) -> None:
        """
            set value to parent variable, need to be `Parent` or `None` type
        """
        if not isinstance(var, Parent) and var is not None:
            raise TypeError("parent must be a `Parent` or `None` type")
        self.__parent = var

    def set_parent(self, parent_value : str) -> None:
        """
            set type by type name,
            type name must be in `Parent` class
        """
        raise NotImplementedError

    @url.setter
    def url(self, var : Optional[str]) -> None:
        """
            set value to url variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("url must be a `str` or `None` type")
        self.__url = var

    @public_url.setter
    def public_url(self, var : Optional[str]) -> None:
        """
            set value to public_url variable, need to be `str` or `None` type
        """
        if not isinstance(var, str) and var is not None:
            raise TypeError("public_url must be a `str` or `None` type")
        self.__public_url = var

