from flask import Flask, jsonify, request

app = Flask(__name__)

receitas = [
    {
        'id': 1,
        'nome': 'ovo frito',
        'modo_preparo': '1- teste | 2 - teste'
    }, 
    {
        'id': 2,
        'nome': 'ovo cozido',
        'modo_preparo': '1- teste | 2 - teste'
    },
]
#Consulta tudo
@app.route('/receitas', methods=['GET'])
def obter_receitas():
    return jsonify(receitas)

#consulta por id
@app.route('/receitas/<int:id>', methods=['GET'])
def obter_receita_por_id(id):
    for receita in receitas:
        if receita.get('id') == id:
            return jsonify(receita)

#edita uma receita
@app.route('/receitas/<int:id>', methods=['PUT'])
def edita_receita_por_id(id):
    receita_alterada = request.get_json()
    for indice, receita in enumerate(receitas):
        receitas[indice].update(receita_alterada)
        return jsonify(receitas[indice])

#incluir nova receita

#excluir receita

app.run(port=5000, host='localhost', debug=True)
