from flask import Flask
from modules.msAuthentication.auth import auth_blueprint
from modules.users.controller import users_controller
from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(users_controller)

Connect().create_tables()
Connect().init_database()

if __name__ == "__main__":
    app.run(debug=True)
