from Chat import Chat
from ChatFactory import ChatIndividualFactory
from Pesquisa import PesquisaParcial

class ChatIndividual(Chat):

    def __init__(self, usuario1, usuario2):

        super().__init__(
            ChatIndividualFactory(), PesquisaParcial()
        )

        self.usuario1 = usuario1
        self.usuario2 = usuario2

        self.ativo = False

    def abrir_chat(self):
        self.ativo = True

    def fechar_chat(self):
        self.ativo = False

    def outro_usuario(self, usuario):
        return (
            self.usuario2
            if self.usuario1 == usuario
            else self.usuario1
        )

    def titulo(self, usuario=None):

        if usuario is None:
            return (
                f"Chat entre "
                f"{self.usuario1.email}"
                f" e "
                f"{self.usuario2.email}"
            )

        return (
            f"Chat com "
            f"{self.outro_usuario(usuario).email}"
        )
