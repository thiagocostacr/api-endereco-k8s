class Endereco:
    def __init__(self, clienteId, logradouro, bairro, cidade, estado, pais, ativo=1):
        self.clienteId = clienteId
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.ativo = ativo
