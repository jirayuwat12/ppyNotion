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


class FormularType(Enum):
    boolean = 1
    date = 2
    number = 3
    string = 4


class MentionType(Enum):
    database = 1
    date = 2
    link_preview = 3
    page = 4
    template_mention = 5
    user = 6


class PropertyType(Enum):
    checkbox = 1
    created_by = 2
    created_time = 3
    date = 4
    email = 5
    files = 6
    formula = 7
    last_edited_by = 8
    last_edited_time = 9
    multi_select = 10
    number = 11
    people = 12
    phone_number = 13
    relation = 14
    rollup = 15
    rich_text = 16
    select = 17
    status = 18
    title = 19
    url = 20


class RollupType(Enum):
    array = 1
    date = 2
    incomplete = 3
    number = 4
    unsupported = 5


class TemplateMentionDateType(Enum):
    today = 1
    now = 2


class TemplateMentionUserType(Enum):
    me = 1
