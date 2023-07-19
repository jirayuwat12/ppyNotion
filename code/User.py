import re
from enum import Enum 
from utils.user import user_id_2_object

class UserType(Enum):
    PERSON = 1
    BOT = 2

class User:

    __userID = None 
    __type = None 
    __name = None 
    __avatar_url = None 
    __person_email = None 
    __bot = None 

    def __init__(self, obj : any) -> None:
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
        if type(obj) == str :
            obj = user_id_2_object(obj)

        if obj['object'] != 'user':
            raise TypeError('object must ne user type object')
        
        # set user id
        self.set_user_id(obj['id'])
        # set type if exist
        if 'type' in obj :
            self.set_type(obj['type'])
        # set name if exist
        if 'name' in obj :
            self.set_name(obj['name'])
        # set avatar url if exist
        if 'avatar_url' in obj :
            self.set_avatar_url(obj['avatar_url'])
        # set person email if type = PERSON
        if self.get_type == UserType.PERSON and 'person' in obj and 'email' in obj['person']:
            self.set_person_email(obj['person']['email'])
        # set bot if type = BOT
        if self.get_type == UserType.BOT and 'bot' in obj:
            self.set_bot(obj['bot'])
            self.set_type(UserType.BOT)

    def __str__(self):
        return f'{self.get_name()}({self.get_user_id()})'

    def set_user_id(self, user_id : str) -> None :
        '''
        set user_id (UUID) to the class if pass the following condition
        1. in form 8-4-4-12 (total 32 characters)
        2. each character be 0-9 or a-f
            
            Parameters:
                user_id (str) : user id
        '''
        if not re.match("[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", user_id):
            raise ValueError(f"user id ({user_id}) must be in UUID form")

        self.__userID = user_id
    
    def set_type(self, type : str) -> None :
        '''
        set type of user

            Parameters:
                type (str) : must be string of 'person' or 'bot' only 
        '''
        if type == "person" :
            self.__type = UserType.PERSON
        elif type == "bot" :
            self.__type = UserType.BOT
        else:
            raise ValueError("type must be either 'bot' or 'person'.")

    def set_name(self, name : str) -> None :
        '''
        set name as show in notion
        '''
        self.__name = name
    
    def set_avatar_url(self, avatar_url : str) -> None : 
        '''
        set avatar url
        '''
        if not re.match(r"^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$", avatar_url) :
            raise ValueError('avatar url must in the standard format')
        
        self.__avatar_url = avatar_url

    def set_person_email(self, person_email : str) -> None :
        '''
        set User email
        must in form (string1)@(string2).(string3)
        '''
        if not re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', person_email):
            raise ValueError('invalid email form')
        
        self.__person_email = person_email

    def set_bot(self, bot : dict) -> None :
        '''
        in case that this user is bot this must not null
        '''
        self.__bot = bot

    def get_user_id(self) -> str:
        return self.__userID
    
    def get_type(self) -> UserType :
        return self.__type
    
    def get_name(self) -> str :
        return self.__name
    
    def get_avatar_url(self) -> str :
        return self.__avatar_url
    
    def get_person_email(self) -> str :
        return self.__person_email
    
    def get_bot(self) -> dict : 
        return self.__bot
    
if __name__ == "__main__":
    import unittest

    class TestUser(unittest.TestCase):
        def test_constructure_1(self):
            # create class from real object
            u = User({
                'object' : 'user',
                'id' : '61111c5a-0000-4ba3-aa3c-a00f0000d5b6'
            })
            self.assertEqual(u.get_user_id(), '61111c5a-0000-4ba3-aa3c-a00f0000d5b6')
            
        def test_set_user_id(self):
            u = User(r'01234567-0123-0123-0123-0123456789ab')
            with self.assertRaises(ValueError):
                u.set_user_id(r'01234567-0123-0123-0123-0123456789ag')
        
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