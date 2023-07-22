'''
`getter_setter_gen.py` use to create getter/setter function for class
'''

from tqdm import tqdm

VAR = \
    '''
__type	str
__id	strorbool
'''


FROM_OBJECT = '    def from_object(self, obj : Dict) -> None:\n'
TO_OBJECT = '    def to_object(self) -> Dict:\n        obj = dict()\n'
GETTER = ''
SETTER = ''

for i in tqdm(VAR.strip().split('\n')):
    name, var_type = i.split()

    GETTER += f'''    @property
    def {name[2:]}(self) -> {var_type}:
        """
            return the {name[2:]}({var_type}) in class
        """
        try :
            self.{name}
        except AttributeError:
            self.{name} = {var_type}{'["default"]' if var_type[-4:] == 'Type' else '()'}
        return self.{name}

'''

    SETTER += f'''    @{name[2:]}.setter
    def {name[2:]}(self, var : Optional[{var_type}]) -> None:
        """
            set value to {name[2:]} variable, need to be `{var_type}` or `None` type
        """
        if not isinstance(var, {var_type}) and var is not None:
            raise TypeError("{name[2:]} must be a `{var_type}` or `None` type")
        self.{name} = var

'''
    if var_type != var_type.lower():
        SETTER += f'''    def set_{name[2:]}(self, {name[2:]}_value : str) -> None:
        """
            set type by type name,
            type name must be in `{var_type}` class
        """
        raise NotImplementedError

'''
    if var_type != var_type.lower():
        FROM_OBJECT += f'''        {name[2:]}_value = obj.get('{name[2:]}')
        if isinstance({name[2:]}_value, {var_type}) or {name[2:]}_value is None:
            self.{name[2:]} = {name[2:]}_value
        else:
            self.set_{name[2:]}({name[2:]}_value)

'''
    else:
        FROM_OBJECT += f'''        self.{name[2:]} = obj.get('{name[2:]}')

'''

TO_OBJECT += '\n        return obj\n'

with open('getter_setter_gen.txt', 'w', encoding='UTF-8') as f:
    f.write(FROM_OBJECT + '\n' + TO_OBJECT + '\n' + GETTER + '\n' + SETTER)

print('saved to `getter_setter_gen.txt')