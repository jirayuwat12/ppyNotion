from typing import Dict
import requests

class Client:
    
    __is_set_token = False 

    def __init__(self, 
                 token : str = "",
                 is_check_token : bool = True
        ) -> None:
        '''
        class that has the important information to access Notion database

            Parameters:
                token (str) : your integraton token from Notion API
                is_check_token (bool) : check the token with Notion API -> raise `ValueError` if invalid

        You can get `token` from https://www.notion.so/my-integrations in your integration or click "+ New integrations"
        '''
        self.set_token(token=token, set_header=True, is_check_token=is_check_token)
    
    def is_valid_token(self, 
                       token : str,
                       check_with_API : bool = True
        ) -> bool:
        '''
        Check if `token` is **valid or not** by the following condition
        1. length of `token` not equal to 0
        2. `token` must start with "secret"

            Paremeters:
                token(str) : your integraton token from Notion API
            Return:
                True if token is valid
                False, other
        '''
         
        #  check with api
        valid_api = True
        if check_with_API:
            response = requests.get(url = r'https://api.notion.com/v1/users/me', headers= {
                "Authorization": "Bearer" + " " + token,
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28"
            })
            valid_api = response.status_code == 200
    
        # check form
        valid_form = len(token) != 0 and token.startswith('secret')

        return valid_form and valid_api

    def __str__(self):
        return f'''client token = {self.get_token()}'''

    def is_set_token(self) -> bool :
        '''
        return `True` if token is setted.
        else return `False`
        '''
        return self.__is_set_token
    
    @property
    def token(self) -> str:
        '''
        get token from class feild
            Return:
                self.__token
        '''
        return self.__token
    
    @property
    def header(self) -> dict:
        '''
        get header for API from class feild
            Return:
                self.__header
        '''
        return self.__header
    
    @token.setter
    def token(self, var : str) -> None:
        self.set_token(token=var)
    
    @header.setter
    def header(self, var : Dict) -> None:
        self.set_token(var['Authorization'].split(' ')[1])
        self.set_header(
            Authorization_prefix = var['Authorization'].split(' ')[0],
            Content_Type = var['Content-Type'],
            Notion_Version = var['Notion-Version']
        )

    def set_token(self, 
                  token : str, 
                  set_header : bool = False,
                  is_check_token : bool = True           
        ) -> None:
        '''
        set `token` if token is valid, raise error in the orther hand.

            Parameters:
                token(str) : your integration token from notion api.
                set_header(bool) : call `self.set_header` after set token if True.
                is_check_token(bool) : check token with API

        '''
        if not self.is_valid_token(token, check_with_API=is_check_token):
            raise ValueError(f"`token`:{token} is not valid.")
        
        self.__token = token
        if set_header:
            self.set_header(is_check_token=is_check_token)
        self.__is_set_token = True 

    def set_header(self,
                    Authorization_prefix : str = "Bearer",
                    Content_Type : str = "application/json",
                    Notion_Version : str = "2022-06-28",
                    is_check_token : bool = True
                ) -> None:
        '''
        set header from token that given to class

            Parameters:
                Authorization_prefix : the prefix that fixed by Notion (default = "Bearer")
                Content_Type : the content type (default = "application/json")
                Notion_Version : Version of Notion API (default = "2022-06-28")
                
        '''
        if not self.is_valid_token(self.token, check_with_API=is_check_token):
            raise ValueError(f"`token`: {self.token} is not valid")
        
        self.__header = {
            "Authorization": Authorization_prefix + " " + self.token,
            "Content-Type": Content_Type,
            "Notion-Version": Notion_Version
        }


if __name__ == "__main__":
    import unittest

    class TestClientClass(unittest.TestCase):
        
        def test_init_invalid_token(self):
            # invalid token
            with self.assertRaises(ValueError):
                obj = Client("123456")

            # empty string token
            with self.assertRaises(ValueError):
                obj = Client()

            # valid string
            token = r"secret....................."
            obj = Client(token, is_check_token=False)
            self.assertTrue(obj.is_valid_token(obj.token, check_with_API=False))
            self.assertEqual(token, obj.token)
        
        def test_geter_setter(self):
            token = r"secret....................."
            obj = Client(token, is_check_token=False)
            self.assertEqual(token, obj.token)
            header = obj.header
            self.assertEqual(header["Authorization"], "Bearer " + token)
            token2 = r"secret1111111111"
            obj.set_token(token2, set_header=True, is_check_token=False)
            self.assertEqual(obj.token, token2)
            header2 = obj.header
            self.assertEqual(header2["Authorization"], "Bearer " + token2)
            obj.set_token(token, is_check_token=False)
            header = obj.header
            self.assertEqual(header["Authorization"], "Bearer " + token2)
    
    unittest.main()
