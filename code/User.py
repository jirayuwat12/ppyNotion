import re
from .utils.user import user_id_2_object

from .Interface.INotionObject import INotionObject
from enum import Enum 
from typing import Dict, Any, Optional

class UserType(Enum):
    person = 1
    bot = 2

class User(INotionObject):

    def __init__(self, obj : Any) -> None:
        '''
        create User class by object that have
        1. 'object' key with the value 'user'
        2. 'id' key with non-empty value
        or the string of user id

            Parameters:
                obj (dict) : obj that commonly got from API
                or obj (str) : user id that you know.
        '''

        # if obj is string -> use utils function to convert into object
        if isinstance(obj, str) :
            obj = user_id_2_object(obj)

        if obj['object'] != 'user':
            raise TypeError('object must ne user type object')
        
        self.from_object(obj)

    def from_object(self, obj : Dict) -> None:
        # set user id
        self.user_id = obj['id']
        # set type if exist
        if 'type' in obj :
            self.type = obj['type']
        # set name if exist
        if 'name' in obj :
            self.name = obj['name']
        # set avatar url if exist
        if 'avatar_url' in obj :
            self.avatar_url = obj['avatar_url']
        # set person email if type = PERSON
        if 'person' in obj:
            if 'email' in obj['person']:
                self.person_email = obj['person']['email']
        # set bot if type = BOT
        if 'bot' in obj:
            self.bot = obj['bot']
    
    def to_object(self) -> Dict:
        ret =  {
            "object" : "user",
            "id" : self.user_id,
        }
        
        if self.type is not None:
            ret['type'] = self.type.name
            if self.type.name == 'person' and self.person_email is not None:
                ret['person'] = dict()
                ret['person']['email'] = self.person_email
            else:
                ret['bot'] = self.bot
        
        if self.name is not None:
            ret['name'] = self.name
        
        if self.avatar_url is not None:
            ret['avatar_url'] = self.avatar_url
        
        return ret

    def __str__(self):
        return f'{self.name}({self.user_id})'
    
    @property
    def user_id(self) -> str:
        return self.__userID
    
    @property
    def type(self) -> UserType :
        return self.__type
    
    @property
    def name(self) -> str :
        return self.__name
    
    @property
    def avatar_url(self) -> str :
        return self.__avatar_url
    
    @property
    def person_email(self) -> str :
        return self.__person_email
    
    @property
    def bot(self) -> Dict : 
        return self.__bot

    @user_id.setter
    def user_id(self, var : str) :
        '''
        set var (UUID) to the class if pass the following condition
        1. in form 8-4-4-12 (total 32 characters)
        2. each character be 0-9 or a-f
            
            Parameters:
                var (str) : user id
        '''
        if not re.match("[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", var):
            raise ValueError(f"user id ({var}) must be in UUID form")

        self.__userID = var
    
    @type.setter
    def type(self, type : str) -> None :
        '''
        set type of user

            Parameters:
                type (str) : must be string of 'person' or 'bot' only 
        '''
        if type == "person" :
            self.__type = UserType.person
        elif type == "bot" :
            self.__type = UserType.bot
        else:
            raise ValueError("type must be either 'bot' or 'person'.")

    @name.setter
    def name(self, name : str) -> None :
        '''
        set name as show in notion
        '''
        self.__name = name
    
    @avatar_url.setter
    def avatar_url(self, avatar_url : str) -> None : 
        '''
        set avatar url
        '''
        if not re.match(r"^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$", avatar_url) :
            raise ValueError('avatar url must in the standard format')
        
        self.__avatar_url = avatar_url

    @person_email.setter
    def person_email(self, person_email : str) -> None :
        '''
        set User email
        must in form (string1)@(string2).(string3)
        '''
        if not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', person_email):
            raise ValueError('invalid email form')
        
        self.__person_email = person_email

    @bot.setter
    def bot(self, bot : Dict) -> None :
        '''
        in case that this user is bot this must not null
        '''
        self.__bot = bot
    
if __name__ == "__main__":
    import unittest

    class TestUser(unittest.TestCase):
        def test_constructure_1(self):
            # create class from real object
            u = User({
                'object' : 'user',
                'id' : '61111c5a-0000-4ba3-aa3c-a00f0000d5b6',
                'type' : 'person',
                'person' :{
                    'email' : 'test@gmail.com'
                }
            })
            self.assertEqual(u.user_id, '61111c5a-0000-4ba3-aa3c-a00f0000d5b6')
            
        def test_set_user_id(self):
            u = User(r'01234567-0123-0123-0123-0123456789ab')
            with self.assertRaises(ValueError):
                u.user_id = r'01234567-0123-0123-0123-0123456789ag'
        
        def test_set_type(self):
            pass

        def test_set_name(self):
            pass

        def test_set_avatar_url(self):
            pass

        def test_set_person_email(self):
            pass

        def test_set_bot(self):
            pass

    unittest.main()