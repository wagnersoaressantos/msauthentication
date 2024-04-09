class SQLUsers:

    _TABLE_NAME = 'users'
    _COL_ID = 'id'
    _COL_NAME = 'name'
    _COL_PASSWORD = 'password'

    _CREATE_TABLE = (f'CREATE TABLE IF NOT EXISTS{_TABLE_NAME} '
                     f'({_COL_ID} SERIAL PRIMARY KEY,'
                     f'{_COL_NAME} VARCHAR(255),'
                     f'{_COL_PASSWORD} VARCHAR(255));')
    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_NAME},{_COL_PASSWORD}) VALUES (%s, %s) RETURNING id;'
    _UPDATE_USER = f'UPDATE {_TABLE_NAME} SET {_COL_NAME} = %s, {_COL_PASSWORD} =%s WHERE {_COL_ID} = %s;'
    _DELETE_USER = f'DELETE FROM {_TABLE_NAME} WHERE {_COL_ID} = %s;'
    _SELECT_ALL = f'SELECT * FROM {_TABLE_NAME}'
    _USERS_VALID = f"SELECT * FROM {_TABLE_NAME} WHERE {_COL_NAME} = %s AND {_COL_PASSWORD} = %s;"