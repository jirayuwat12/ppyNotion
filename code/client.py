import requests

class Client:
    
    __token = ""
    __header = ""

    def __init__(self, token : str = "") -> None:
        '''
        class that has the important information to access Notion database

            Parameters:
                token(str) : your integraton token from Notion API

        You can get `token` from https://www.notion.so/my-integrations in your integration or click "+ New integrations"
        '''
        if not self.is_valid_token(token):    
            raise ValueError(f"`token`:{token} is not valid.")
        self.set_token(token=token)

    def is_valid_token(self, token : str) -> bool:
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
        if len(token) != 0 and token.startswith('secret'):
            return True
        else:
            return False
        
    def get_token(self) -> str:
        '''
        get token from class feild
            Return:
                self.__token
        '''
        return self.__token
    
    def get_header(self) -> dict:
        '''
        get header for API from class feild
            Return:
                self.__header
        '''
        return self.__header
    
    def set_token(self, token : str, set_header : bool = True) -> None:
        '''
        set `token` if token is valid, raise error in the orther hand.

            Parameters:
                token(str) : your integration token from notion api.
                set_header(bool) : call `self.set_header` after set token if True.

        '''
        if not self.is_valid_token(token):
            raise ValueError(f"`token`:{token} is not valid.")
        
        self.__token = token
        if set_header:
            self.set_header()

    def set_header(self,
                    Authorization_prefix : str = "Bearer",
                    Content_Type : str = "application/json",
                    Notion_Version : str = "2022-06-28"
                ) -> None:
        '''
        set header from token that given to class

            Parameters:
                Authorization_prefix : the prefix that fixed by Notion (default = "Bearer")
                Content_Type : the content type (default = "application/json")
                Notion_Version : Version of Notion API (default = "2022-06-28")
                
        '''
        if not self.is_valid_token(self.get_token()):
            raise ValueError(f"`token`: {self.get_token()} is not valid")
        
        self.__header = {
            "Authorization": Authorization_prefix + " " + self.__token,
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
            obj = Client(token)
            self.assertTrue(obj.is_valid_token(obj.get_token()))
            self.assertEqual(token, obj.get_token())
        
        def test_geter_setter(self):
            token = r"secret....................."
            obj = Client(token)
            self.assertEqual(token, obj.get_token())
            header = obj.get_header()
            self.assertEqual(header["Authorization"], "Bearer " + token)
            token2 = r"secret1111111111"
            obj.set_token(token2)
            self.assertEqual(obj.get_token(), token2)
            header2 = obj.get_header()
            self.assertEqual(header2["Authorization"], "Bearer " + token2)
            obj.set_token(token, False)
            header = obj.get_header()
            self.assertEqual(header["Authorization"], "Bearer " + token2)
    
    unittest.main()
