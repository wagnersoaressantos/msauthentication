from modules.users.user_sql import SQLUsers
from service.connect import Connect


class DAOUsers(SQLUsers):

    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE
    def verify_credentials(self, username, password):
        query = self._USERS_VALID
        cursor = self.connection.cursor()
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        return result is not None
