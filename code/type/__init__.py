'''
Collection of Enumerator class.
'''
from enum import Enum


class UserType(Enum):
    '''
    Enum for type of User 
    '''
    person = 1
    bot = 2


class ColorType(Enum):
    '''
    Enum for type of Color
    '''
    default = 1
    blue = 2
    brown = 3
    gray = 4
    green = 5
    orange = 6
    pink = 7
    purple = 8
    red = 9
    yellow = 10
    blue_background = 11
    brown_background = 12
    gray_background = 13
    green_background = 14
    orange_background = 15
    pink_background = 16
    purple_background = 17
    red_background = 18
    yellow_background = 19


class BaseTextType(Enum):
    '''
    Enum for type of Rich text
    '''
    text = 1
    mention = 2
    equation = 3
