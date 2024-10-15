from flask import Blueprint, jsonify, request

route_bp = Blueprint('route', __name__)

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
@route_bp.route('/receitas', methods=['GET'])
def obter_receitas():
    return jsonify(receitas)

#consulta por id
@route_bp.route('/receitas/<int:id>', methods=['GET'])
def obter_receita_por_id(id):
    for receita in receitas:
        if receita.get('id') == id:
            return jsonify(receita)

#edita uma receita
@route_bp.route('/receitas/<int:id>', methods=['PUT'])
def edita_receita_por_id(id):
    receita_alterada = request.get_json()
    for indice, receita in enumerate(receitas):
        receitas[indice].update(receita_alterada)
        return jsonify(receitas[indice])

#incluir nova receita
@route_bp.route('/receitas', methods=['POST'])
def incluir_nova_receita():
    nova_receita = request.get_json()
    receitas.append(nova_receita)
    
    return jsonify(receitas)

#excluir receita
@route_bp.route('/receitas/<int:id>', methods=['DELETE'])
def excluir_receitas(id):
    for indice, receita in enumerate(receitas):
        if receita.get('id') == id:
            del receitas[indice]
    
    return jsonify(receitas)