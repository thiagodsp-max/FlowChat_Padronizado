from Enquete import Enquete
from Evento import Evento

class Chat:
    def __init__(self):
        self.mensagens = []
        self.enquetes = []
        self.eventos = []

    def enviar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)

    def enviar_mensagem_temporaria(self, mensagem, segundos=5):
        mensagem.definir_tempo_expiracao(segundos)
        self.mensagens.append(mensagem)

    def remover_mensagens_expiradas(self):
        self.mensagens = [m for m in self.mensagens if not m.expirou()]

    def listar_mensagens(self):
        self.remover_mensagens_expiradas()
        for i, mensagem in enumerate(self.mensagens, start=1):
            mensagem.exibir(i)

    def pesquisar_mensagens(self, termo):
        self.remover_mensagens_expiradas()
        return [m for m in self.mensagens if termo.lower() in m.conteudo.lower()]

    def fixar_mensagem(self, indice):
        if indice < 1 or indice > len(self.mensagens):
            return False

        mensagem = self.mensagens.pop(indice - 1)
        mensagem.fixar()
        self.mensagens.insert(0, mensagem)
        return True

    def reagir_mensagem(self, indice, reacao):
        if indice < 1 or indice > len(self.mensagens):
            return False

        self.mensagens[indice - 1].add_reacao(reacao)
        return True

    def criar_enquete(self, pergunta):
        enquete = Enquete(pergunta)
        self.enquetes.append(enquete)
        return enquete

    def criar_evento(self, nome, data, organizador, descricao):
        evento = Evento(nome, data, organizador, descricao)
        self.eventos.append(evento)
        return evento

    def listar_eventos(self):
        return self.eventos

    def listar_enquetes(self):
        return self.enquetes

    def titulo(self, usuario=None):
        return "Chat"