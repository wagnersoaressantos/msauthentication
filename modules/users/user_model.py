class UserModel():
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password