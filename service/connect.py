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
    
    def init_database(self, version = 'v1'):
        if version == 'v1':
            self.create_table()
        if version == 'v2':
            self.update_database()
            
    def update_database(self):
        pass