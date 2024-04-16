# URL do endpoint de validação de token no sistema de autenticação
AUTH_VALIDATION_URL = "http://localhost:5000/api/v1/authentication/validation/"

# Lista de funcionários (poderia ser substituída por uma base de dados)
employees = [
    {'id': 1, 'name': 'Heldon Jose', 'role': {'id': 1, 'title': 'Desenvolvedor'}},
    {'id': 2, 'name': 'João Jose', 'role': {'id': 1, 'title': 'Desenvolvedor'}},
    {'id': 3, 'name': 'João Maria', 'role': {'id': 2, 'title': 'Analista'}}
]

def get_employees():
    token = request.headers.get('ms-authentication')
    if not token or not validate_token(token):
        return jsonify({'error': 'Token invalido'}), 400
    return jsonify({'response': employees}), 200

def validate_token(token):
    response = requests.post(AUTH_VALIDATION_URL, json={'token': token})
    if response.status_code != 200:
        return False
    return True