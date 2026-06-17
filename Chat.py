from abc import ABC
from datetime import datetime

#A Superclasse de Chat Individual e Chat de Grupo

class Chat(ABC):
    def __init__(self, factory, estrategia_pesquisa):
        self.factory = factory
        self.estrategia_pesquisa = estrategia_pesquisa
        self.mensagens = []
        self.enquetes = []
        self.eventos = []

    def enviar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)

    def criar_mensagem(self, remetente, conteudo):
        mensagem = self.factory.criar_mensagem(remetente,conteudo)
        self.mensagens.append(mensagem)
        return mensagem

    def criar_evento(self,nome,data,organizador,descricao):
        evento = self.factory.criar_evento(nome,data,organizador,descricao)
        self.eventos.append(evento)
        return evento

    def criar_enquete(self, pergunta):
        enquete = self.factory.criar_enquete(pergunta)
        self.enquetes.append(enquete)
        return enquete

    def listar_eventos(self):
        return self.eventos

    def listar_enquetes(self):
        return self.enquetes
    
    def remover_mensagens_expiradas(self):
        self.mensagens = [
            msg for msg in self.mensagens
            if not msg.expirou()]

    def fixar_mensagem(self, indice):
        if indice < 1 or indice > len(self.mensagens):
            return False
        mensagem = self.mensagens.pop(indice - 1)
        mensagem.fixar_mensagem()
        self.mensagens.insert(0,mensagem)
        return True

    def reagir_mensagem(self,indice,reacao):
        if indice < 1 or indice > len(self.mensagens):
            return False
        self.mensagens[indice - 1].add_reacao(reacao)
        return True

    def pesquisar_mensagens(self, termo):
        self.remover_mensagens_expiradas()
        return self.estrategia_pesquisa.pesquisar(self.mensagens, termo)
    
    def definir_estrategia_pesquisa(self,estrategia):
        self.estrategia_pesquisa = estrategia

    def enviar_mensagem_temporaria(self,mensagem,segundos=5):
        mensagem.definir_tempo_expiracao(segundos)
        self.mensagens.append(mensagem)

    '''#Possibilidade
    def registrar_mensagem(self,remetente,conteudo):
        mensagem = self.criar_mensagem(remetente,conteudo)
        if "@todos" in conteudo:
            self.mencionar_todos(remetente)
        return mensagem
    '''
