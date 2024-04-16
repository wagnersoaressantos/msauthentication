from flask import Blueprint, request, jsonify
from modules.roles.dao import DAORole
from modules.roles.modelo import Role

role_controller = Blueprint('role_controller', __name__)
dao_role = DAORole()
module_name = 'roles'

def create_role():
    roles = request.json
    print(roles)
    erros = []
    for data in roles:
        print(data)
        for campo in SQLRole._CAMPOS_OBRIGATORIOS:
            if campo not in data.keys() or not data.get(campo, '').strip():
                erros.append(f'O campo {campo} deve ser preenchido')
            if dao_role.get_roles_by_title(data.get("title")):
                erros.append(f'Já existe uma função com o titulo {data.get("title")}')
            if erros:
                response = jsonify(erros)
                response.status_code =401
                return response
        role = Role(**data)
        role = dao_role.salvar(role)
        print(role)
    response = jsonify('sucesso')
    response.status_code = 201
    return response

def get_role():
    roles = dao_role.get_all()
    results = [role.__dict__ for role in roles]
    response = jsonify(results)
    response.status_code = 200
    return response

@roles_controller.route(f'/{module_name}/', methods=['GET','POST'])
def get_or_create_role():
    if request.method == 'GET':
        return get_role()
    else:
        return create_role()