import requests

class Client:
    
    __token = ""
    __header = ""

    def __init__(self, token : str = "") -> None:
        '''
        You can get `token` from https://www.notion.so/my-integrations in your integration or click "+ New integrations"
        '''
        if self.is_valid_token(token):
            self.set_token(token=token)
    
    def is_valid_token(self, token : str):
        '''
        Check if `token` is **valid or not** by the following condition
        1. length of `token` not equal to 0
        1. `token` must start with "secret"
        '''
        if len(token) != 0 and token.startswith('secret'):
            return True
        else:
            return False
        
    def get_token(self) -> str:
        return self.__token
    
    def get_header(self) -> dict:
        return self.__header
    
    def set_token(self, token : str, set_header : bool = True) -> None:
        '''
        set `token` if token is valid, raise error in the orther hand.

            Parameters:
                token(str) : your integration token from notion api.
                set_header(bool) : call `self.set_header` after set token if True.

        '''
        if not self.is_valid_token(token):
            raise ValueError("`token` must be valid.")
        
        self.__token = token
        if set_header:
            self.set_header()

    def set_header(self) -> None:
        self.__header = {
            "Authorization": "Bearer " + self.__token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }