import requests
from flask import jsonify, request
from dao import EnderecoDAO
from models import Endereco
from app import app, db

endereco_dao = EnderecoDAO(db)
@app.route('/endereco', methods=['GET'])
def listar():
    endereco = endereco_dao.listarEndereco()
    resultado = formataRetornoHelper(endereco)
    return jsonify(resultado), 200

@app.route('/endereco/<int:enderecoid>', methods=['GET'])
def listarId(enderecoid):
    if enderecoid:
        endereco = endereco_dao.listarEnderecoId(enderecoid)
        resultado = formataRetornoHelper(endereco)
        return jsonify(resultado), 200
    else:
        return jsonify('endereco não encontrado'), 200

@app.route('/endereco/<int:clientid>', methods=['POST'])
def inserir(clientid):
    r = requests.get(app.config['CLIENTE_ENDPOINT'] + '/' + str(clientid))
    cliente = r.json()
    data = request.json
    if cliente['id'] == clientid and data['clienteid']:
        endereco = Endereco(data['clienteid'], data['logradouro'], data['bairro'], data['cidade'], data['estado'], data['pais'])
        endereco_dao.inserirEndereco(endereco)
        return jsonify("endereco cadastrado com sucesso"), 200
    else:
        return jsonify('problemas ao cadastrar endereço')

@app.route('/endereco/<int:enderecoid>', methods=['PUT'])
def atualizar(enderecoid):
    data = request.json
    if endereco_dao.listarEnderecoId(enderecoid):
        endereco = Endereco(data['clienteid'], data['logradouro'], data['bairro'], data['cidade'], data['estado'], data['pais'])
        endereco_dao.atualizarEndereco(enderecoid, endereco)
        return jsonify('endereco atualizado com sucesso'), 200
    else:
        return jsonify('problemas ao atualizar o endereco'), 404

@app.route('/endereco/<int:enderecoid>', methods=['DELETE'])
def excluir(enderecoid):
    if enderecoid:
        endereco_dao.excluirEndedeco(enderecoid)
        return jsonify('endereco excluido com sucesso'), 200
    else:
        return jsonify('problemas ao excluir enderecio'), 400


def formataRetornoHelper(endereco):
    resultado = []
    for row in endereco:
        resultado.append({'id': row[0], 'clienteid': row[1], 'logradouro': row[2], 'bairro': row[3], 'cidade': row[4], 'estado': row[5], 'pais': row[6]})
    return resultado
