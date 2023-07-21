import requests
import json
from .utils.date_formatter import ISO8601_to_datetime
from datetime import datetime

from typing import AnyStr, Dict
from .Client import Client
from .User import User
from .Interface.i_notion_object import INotionObject

class Database(INotionObject):

    API_URL = f"https://api.notion.com/v1/databases/"
    __database_id = None 
    __client = None 
    __created_time = None 
    __created_by = None 
    __last_edited_time = None 
    __last_edited_by = None 
    __title = None 
    __description = None 
    __icon = None 
    __cover = None 
    __properties = None 
    __parent = None 
    __archived = None 
    __is_inline = None 
    __public_url = None 
    __pages = None

    def __init__(self, 
                 client : Client = None,
                 database_id : AnyStr = None,
                 obj : Dict = None,
                 load_data : bool = True
            ) -> None :
        '''
        
        '''

        # set client class
        if client is not None:
            self.set_client(client= client)

        # set database id
        if database_id is not None:
            self.set_database_id(databse_id= database_id)

        if not load_data or obj is not None: 
            return
        
        # get data from api
        if load_data:
            response = requests.get(self.API_URL + database_id, headers= client.get_header())
            if response.status_code != 200 :
                raise ConnectionError(f"status code = {response.status_code}\nerror = {response}")

        # convert to object  
        response_json = json.loads(response.text) if load_data else obj
        
        self.from_object(response_json)

    def from_object(self, obj : Dict) -> None:
        '''
        set class field by obj in form notion api like.
        
            Parameters:
                obj(dict) : object that has at least `id` key. Other please see at Notion API
        '''
        # set created time if exist
        if 'created_time' in obj:
            self.set_created_time(obj['created_time'])

        # set created by if exist
        if 'created_by' in obj:
            created_user = User(obj['created_by'])
            self.set_created_by(created_user)

        # set last edited time if exist
        if 'last_edited_time' in obj:
            self.set_last_edited_time(obj['last_edited_time'])

        # set last edited time if exist
        if 'last_edited_by' in obj:
            last_edited_user = User(obj['last_edited_by'])
            self.set_last_edited_by(last_edited_user)

    def to_object(self) -> Dict:
        pass

    def __str__(self):
        return f'database id = {self.get_database_id()} \
            \n{self.get_client()} \
            \ncreated time = {self.get_created_time()} \
            \ncreated by = {self.get_created_by()} \
            \nlast edited time = {self.get_last_edited_time()} \
            \nlast edited by = {self.get_last_edited_by()} \
        '
            
    def set_database_id(self, databse_id : str) -> None :
        '''
        set database id that suit the conditions
        1. is 32 characters alphanumeric string

            Parameters:
                database_id (str) : get from url 
        '''
        if len(databse_id) != 32 :
            raise ValueError(f"database id ({databse_id}) is not 32 characters alphanumeric string\nlink : https://developers.notion.com/reference/retrieve-a-database")
        
        self.__database_id = databse_id

    def set_client(self, client : Client) -> None :
        '''
        set client only if client onject has been set token.

            Parameters:
                client (Client) : must create client onject before.
        '''
        if not client.is_set_token() :
            raise AttributeError("Client object must set token first.")

        self.__client = client

    def set_created_time(self, created_time : str) -> None :
        '''
        set created time
            
            Parameters:
                created_time (str) : string time in ISO 8601 date and time format
        '''
        self.__created_time = ISO8601_to_datetime(created_time)

    def set_created_by(self, created_by : User) -> None :
        '''
        set user that created the database 

            Parameters:
                created_by (User) : user that created the database
        '''
        self.__created_by = created_by

    def set_last_edited_time(self, last_edited_time : str) -> None :
        '''
        set last_edited time
            
            Parameters:
                last_edited_time (str) : string time in ISO 8601 date and time format
        '''
        self.__last_edited_time = ISO8601_to_datetime(last_edited_time)

    def set_last_edited_by(self, last_edited_by : User) -> None :
        '''
        set user that last edited the database 

            Parameters:
                last_edited_by (User) : user that last edited the database
        '''
        self.__last_edited_by = last_edited_by
    

    def get_database_id(self) -> str :
        return self.__database_id

    def get_client(self) -> Client : 
        return self.__client

    def get_created_time(self) -> datetime :
        return self.__created_time

    def get_created_by(self) -> User : 
        return self.__created_by

    def get_last_edited_time(self) -> datetime :
        return self.__last_edited_time
    
    def get_last_edited_by(self) -> User :
        return self.__last_edited_by


if __name__ == "__main__":
    
    obj = None
    with open('./secret.txt','r') as f:
        obj = json.loads(f.read())
    token = obj['token']
    dbid = obj['dbid']

    client = Client(token)
    db = Database(client, dbid)

    u = db.get_created_by()


    print(db)