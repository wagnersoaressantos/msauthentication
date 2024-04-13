from flask import Flask
from modules.msAuthentication.auth import auth_blueprint
from modules.roles.controller import role_controller

from modules.employees.controller import employees_controller
from service.connect import Connect

app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(role_controller)
app.register_blueprint(employees_controller)


Connect().create_table()
Connect().init_database()

if __name__ == "__main__":
    app.run(debug=True)
