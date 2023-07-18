import requests
import json
from utils import ISO8601_to_datetime
from datetime import datetime

from Client import Client

class Database:

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
                 client : Client,
                 database_id : str,
                 load_data : bool = True
            ) -> None :
        '''
        
        '''
        self.set_client(client= client)
        self.set_database_id(databse_id= database_id)

        if not load_data : 
            return
        
        response = requests.get(self.API_URL + database_id, headers= client.get_header())
        if response.status_code != 200 :
            raise ConnectionError(f"status code = {response.status_code}\nerror = {response}")
        
        response_json = json.loads(response.text)

        self.set_created_time(response_json['created_time'])

    def __str__(self):
        return f'database id = {self.get_database_id()} \
            \n{self.get_client()} \
            \ncreated time = {self.get_created_time()} \
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

    def set_created_time(self, created_time : str) -> None:
        '''
        set created time
            
            Parameters:
                created_time (str) : string time in ISO 8601 date and time format
        '''
        self.__created_time = ISO8601_to_datetime(created_time)

    def get_database_id(self) -> str :
        return self.__database_id

    def get_client(self) -> Client : 
        return self.__client

    def get_created_time(self) -> datetime :
        return self.__created_time


if __name__ == "__main__":
    
    obj = None
    with open('../secret.txt','r') as f:
        obj = json.loads(f.read())
    token = obj['token']
    dbid = obj['dbid']

    client = Client(token)
    db = Database(client, dbid)

    print(db)