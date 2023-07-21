'''
`getter_setter_gen.py` use to create getter/setter function for class
'''
from tqdm import tqdm

VAR = \
    '''
__user_id	str
__type	UserType
__name	str
__avatar_url	str
__person_email	str
__bot	dict
'''

GETTER = ''
SETTER = ''

for i in tqdm(VAR.strip().split('\n')):
    name, var_type = i.split()

    GETTER += f'@property\
\ndef {name[2:]}(self) -> {var_type}:\
\n    """\
\n        return the {name[2:]}({var_type}) in class\
\n    """\
\n    try :\
\n        self.{name}\
\n    except AttributeError:\
\n        self.{name} = {var_type}()\
\n    return self.{name}\
\n\n'

    SETTER += f'@{name[2:]}.setter\
\ndef {name[2:]}(self, var : {var_type}) -> None:\
\n    """\
\n        set value to {name[2:]} variable, need to be `{var_type}` type\
\n    """\
\n    if not isinstance(var, {var_type}):\
\n        raise TypeError("{name[2:]} must be a `{var_type}` type")\
\n    self.{name} = var\
\n\n'

print(GETTER, SETTER, sep='\n')
with open('getter_setter_gen.txt', 'w', encoding='UTF-8') as f:
    f.write(GETTER + '\n' + SETTER)
