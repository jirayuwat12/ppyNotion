
def user_id_2_object(user_id : str) -> dict:
    '''
    create user object from user id without check the validity of user_id
    '''
    ret = {
        'object' : 'user',
        'id' : user_id
    }

    return ret