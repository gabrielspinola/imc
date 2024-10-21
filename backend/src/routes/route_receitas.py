from flask import Blueprint, jsonify, request
import jwt

route_receitas = Blueprint('route_receitas', __name__)

receitas = [
    {
        "id": 1,
        "nome": "ovo frito",
        "modo_preparo": "1- teste | 2 - teste"
    }, 
    {
        "id": 2,
        "nome": "ovo cozido",
        "modo_preparo": "1- teste | 2 - teste"
    },
]
#Consulta tudo
@route_receitas.route('/receitas', methods=['GET'])
def obter_receitas():
    raw_token = request.headers.get("Authorization")
    uid = request.headers.get("uid")
    
    if not raw_token or not uid:
        return jsonify({
            'error' : 'Não Autorizado!'
            }), 400
        
    try:
        token = raw_token.split()[1]
        token_information = jwt.decode(token, key='1234', algorithms='HS256')
        token_uid = token_information["uid"]
    except jwt.InvalidSignatureError:
        return jsonify({
            'error': 'Token Invalido!'
        }), 401
    except jwt.ExpiredSignatureError: 
        return jsonify({
            'error': 'Token Expirado!'
        }), 401
        
    if int(token_uid) != int(uid):
        return jsonify({
           'error': 'Token Expirado!'
        }), 400
    
    print(token_information)
    return jsonify(receitas)

#consulta por id
@route_receitas.route('/receitas/<int:id>', methods=['GET'])
def obter_receita_por_id(id):
    for receita in receitas:
        if receita.get('id') == id:
            return jsonify(receita)

#edita uma receita
@route_receitas.route('/receitas/<int:id>', methods=['PUT'])
def edita_receita_por_id(id):
    receita_alterada = request.get_json()
    for indice, receita in enumerate(receitas):
        receitas[indice].update(receita_alterada)
        return jsonify(receitas[indice])

#incluir nova receita
@route_receitas.route('/receitas', methods=['POST'])
def incluir_nova_receita():
    nova_receita = request.get_json()
    receitas.append(nova_receita)
    
    return jsonify(receitas)

#excluir receita
@route_receitas.route('/receitas/<int:id>', methods=['DELETE'])
def excluir_receitas(id):
    for indice, receita in enumerate(receitas):
        if receita.get('id') == id:
            del receitas[indice]
    
    return jsonify(receitas)