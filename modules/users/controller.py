from flask import Blueprint, request, jsonify
from modules.users.dao import DAOUsers
from modules.users.user_model import UserModel
from modules.users.user_sql import SQLUsers

users_controller = Blueprint('users_controller', __name__)
dao_users = DAOUsers()
module_name = 'users'

def user_padrao():
    user_padrao = 'admin'
    password_padrao = 'admin'
    if(not dao_users.get_user_name(user_padrao)):
        user_padrao = UserModel(username= user_padrao, password=password_padrao)
        dao_users.salvar(user_padrao)
        return jsonify('base iniciada com sucesso')
    return jsonify('base iniciada com sucesso')

def create_user():
    users = request.json
    error = []
    for data in users:
        for campo in SQLUsers._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                error.append(f'{campo} is required.')
        if error:
            response = jsonify(error)
            response.status_code = 401
            return response
        user = UserModel(**data)
        dao_users.salvar(user)
    response = jsonify('User criado com sucesso!')
    response.status_code = 201
    return response