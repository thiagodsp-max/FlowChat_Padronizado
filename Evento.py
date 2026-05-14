#Classe para os Eventos

class Evento:
    def __init__(self, nome, data, organizador, descricao):
        self.nome = nome
        self.data = data
        self.organizador = organizador
        self.descricao = descricao
        self.status = "programado"

    def cancelar(self, usuario):
        if self.organizador != usuario:
            return False
        self.status = "cancelado"
        return True

    def editar(self, usuario, nome=None, data=None, descricao=None, status=None):
        if self.organizador != usuario:
            return False

        if nome:
            self.nome = nome
        if data:
            self.data = data
        if descricao:
            self.descricao = descricao
        if status:
            self.status = status

        return True