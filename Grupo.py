from Chat import Chat
from ChatFactory import ChatGrupoFactory
from Pesquisa import PesquisaPorRemetente

class Grupo(Chat):

    def __init__(self, nome=None):
        super().__init__(ChatGrupoFactory(), PesquisaPorRemetente())
        self.nome = nome
        self.membros = []
        self.notificacoes = {}

    def add_membro(self, usuario):

        if usuario not in self.membros:

            self.membros.append(usuario)

            self.notificacoes[
                usuario.email
            ] = 0

    def mencionar_todos(self, remetente):

        for membro in self.membros:

            if membro != remetente:

                self.notificacoes[
                    membro.email
                ] += 1

    def qtd_notificacoes(self, usuario):
        return self.notificacoes.get(usuario.email,0)

    def limpar_notificacoes(self, usuario):
        self.notificacoes[usuario.email] = 0

    def titulo(self, usuario=None):
        return f"Grupo: {self.nome}"
    
    def criar_mensagem(self,remetente,conteudo):
        mensagem = super().criar_mensagem(remetente,conteudo)
        if "@todos" in conteudo:
            self.mencionar_todos(remetente)
        return mensagem
