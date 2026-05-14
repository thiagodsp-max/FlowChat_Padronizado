from Chat import Chat
from Mensagem import MensagemGrupo

class Grupo(Chat):
    def __init__(self, nome=None):
        super().__init__()
        self.nome = nome
        self.membros = []
        self.notificacoes = {}

    def criar_grupo(self, nome):
        self.nome = nome

    def add_membro(self, usuario):
        if usuario not in self.membros:
            self.membros.append(usuario)
            self.notificacoes[usuario.email] = 0

    def criar_mensagem(self, remetente, conteudo):
        return MensagemGrupo(remetente, conteudo)

    def mencionar_todos(self, remetente):
        for membro in self.membros:
            if membro != remetente:
                self.notificacoes[membro.email] += 1

    def registrar_mensagem(self, remetente, conteudo):
        mensagem = self.criar_mensagem(remetente, conteudo)
        self.enviar_mensagem(mensagem)

        if "@todos" in conteudo:
            self.mencionar_todos(remetente)

        return mensagem

    def limpar_notificacoes(self, usuario):
        self.notificacoes[usuario.email] = 0

    def qtd_notificacoes(self, usuario):
        return self.notificacoes.get(usuario.email, 0)

    def titulo(self, usuario=None):
        return f"Grupo: {self.nome}"