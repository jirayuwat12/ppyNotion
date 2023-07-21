from tqdm import tqdm 

var = \
'''
__bold	bool
__italic	bool
__strikethrough	bool
__underline	bool
__code	bool
__color	ColorType
'''

getter = ''
setter = ''

for i in tqdm(var.strip().split('\n')):
    name, var_type = i.split()
    
    getter += f'@property \
    \ndef {name[2:]}(self) -> {var_type}: \
    \n    """\
    \n        return the {name[2:]}({var_type}) in class\
    \n    """\
    \n    try : self.{name}\
    \n    except : self.{name} = None\
    \n    return self.{name}\
    \n\n'

    setter += f'@{name[2:]}.setter \
    \ndef {name[2:]}(self, var : {var_type}) -> None:\
    \n    """\
    \n        set value to {name[2:]} variable, need to be `{var_type}` type\
    \n    """\
    \n    if not isinstance(var, {var_type}):\
    \n        raise TypeError(f"{name[2:]} must be a `{var_type}` type")\
    \n    self.{name} = var\
    \n\n'

print(getter, setter, sep = '\n')
with open('getter_setter_gen.txt','w') as f:
    f.write(getter + '\n' + setter)