from models import Endereco

INSERE_ENDERECO='insert into endereco(clienteid, logradouro, bairro, cidade, estado, pais, ativado) values (%s, %s, %s, %s, %s, %s, %s)'
LISTAR_ENDERECO='select * from endereco where ativado = 1'
LISTAR_ENDERECO_ID='select * from endereco where id = %s'
ATUALIZAR_ENDERECO='update endereco set clienteId=%s, logradouro=%s, bairro=%s, cidade=%s, estado=%s, pais=%s where clienteid=%s and id=%s and ativado=1'
EXCLUIR_ENDERECO='update endereco set ativado = 0 where id = %s and ativado = 1'
class EnderecoDAO:
    def __init__(self, db):
        self.__db = db

    def inserirEndereco(self, endereco):
        cursor = self.__db.connection.cursor()
        cursor.execute(INSERE_ENDERECO, (endereco.clienteId, endereco.logradouro, endereco.bairro, endereco.cidade, endereco.estado, endereco.pais, 1))
        self.__db.connection.commit()

    def listarEndereco(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_ENDERECO)
        endereco = cursor.fetchall()
        return endereco

    def listarEnderecoId(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(LISTAR_ENDERECO_ID, (id,))
        endereco = cursor.fetchall()
        return endereco

    def atualizarEndereco(self, id, endereco):
        cursor = self.__db.connection.cursor()
        cursor.execute(ATUALIZAR_ENDERECO, (endereco.clienteId, endereco.logradouro, endereco.bairro, endereco.cidade, endereco.estado, endereco.pais, endereco.clienteId, id))
        self.__db.connection.commit()
        return endereco

    def excluirEndedeco(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(EXCLUIR_ENDERECO, (id,))
        self.__db.connection.commit()
