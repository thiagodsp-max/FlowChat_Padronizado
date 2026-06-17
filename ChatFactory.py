from Mensagem import (Mensagem,LeituraMensagemPrivada,LeituraMensagemGrupo)
from Evento import Evento
from Enquete import Enquete
from abc import ABC, abstractmethod

class ChatFactory(ABC):
    @abstractmethod
    def criar_mensagem(self, remetente, conteudo):
        pass

    @abstractmethod
    def criar_evento(self, nome, data, organizador, descricao):
        pass

    @abstractmethod
    def criar_enquete(self, pergunta):
        pass

class ChatIndividualFactory(ChatFactory):
    def criar_mensagem(self, remetente, conteudo):
        return Mensagem(remetente,conteudo,LeituraMensagemPrivada())

    def criar_evento(self, nome, data, organizador, descricao):
        return Evento(nome, data, organizador, descricao)

    def criar_enquete(self, pergunta):
        return Enquete(pergunta)

class ChatGrupoFactory(ChatFactory):
    def criar_mensagem(self, remetente, conteudo):
        return Mensagem(remetente,conteudo,LeituraMensagemGrupo())

    def criar_evento(self, nome, data, organizador, descricao):
        return Evento(nome, data, organizador, descricao)

    def criar_enquete(self, pergunta):
        return Enquete(pergunta)
