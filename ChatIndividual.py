from Chat import Chat
from Mensagem import MensagemPrivada

class ChatIndividual(Chat):
    def __init__(self, usuario1, usuario2):
        super().__init__()
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.ativo = False

    def abrir_chat(self):
        self.ativo = True

    def fechar_chat(self):
        self.ativo = False

    def criar_mensagem(self, remetente, conteudo):
        return MensagemPrivada(remetente, conteudo)

    def outro_usuario(self, usuario):
        return self.usuario2 if self.usuario1 == usuario else self.usuario1

    def titulo(self, usuario=None):
        if usuario is None:
            return f"Chat entre {self.usuario1.email} e {self.usuario2.email}"
        return f"Chat com {self.outro_usuario(usuario).email}"

    def visualizar_mensagens(self, usuario):
        for mensagem in self.mensagens:
            if isinstance(mensagem, MensagemPrivada) and mensagem.remetente != usuario:
                mensagem.marcar_como_visualizada()