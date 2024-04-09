import psycopg2



class Connect:
    def __init__(self):
        config = dict(dbname="MS_Authentication",
                      user="postgres", password="redgaw",
                      host="localhost", port="5432")
        self._connection = psycopg2.connect(**config)

    def create_table(self):
        from modules.users.dao import DAOUsers
        cursor = self._connection.cursor()
        cursor.execute(DAOUsers().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection