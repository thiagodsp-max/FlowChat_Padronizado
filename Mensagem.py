#Classe com o Padrão Criacional Abstract Factory
from abc import ABC, abstractmethod

#Abstract Product
class Mensagem(ABC):
    def __init__(self, remetente, conteudo):
        self.remetente = remetente
        self.conteudo = conteudo
        self.reacoes = []
        self.fixada = False
        self.expira_em = None

    def add_reacao(self, reacao):
        self.reacoes.append(reacao)

    def fixar(self):
        self.fixada = True

    def definir_tempo_expiracao(self, segundos):
        import time
        self.expira_em = time.time() + segundos

    def expirou(self):
        import time
        return self.expira_em is not None and time.time() >= self.expira_em

    def formatar_reacoes(self):
        if not self.reacoes:
            return ""
        return " (" + " ".join(self.reacoes) + " )"

    def exibir(self, indice=None):
        prefixo = f"{indice} - " if indice is not None else ""
        fixada = "[FIXADA] " if self.fixada else ""
        print(f"{fixada}{prefixo}{self.remetente.email}: {self.conteudo}{self.formatar_reacoes()}")

    @abstractmethod
    def marcar_como_lida():
        pass

#Concrete Product A
class MensagemGrupo(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.lida_por = []

    def marcar_como_lida(self, usuario):
        if usuario.email not in self.lida_por:
            self.lida_por.append(usuario.email)

#Concrete Product B
class MensagemPrivada(Mensagem):
    def __init__(self, remetente, conteudo):
        super().__init__(remetente, conteudo)
        self.visualizada = False

    def marcar_como_lida(self):
        self.visualizada = True

#Concrete Factory A
class FactoryGrupo:
    @staticmethod
    def criar_mensagem(remetente, conteudo):
        return MensagemGrupo(remetente, conteudo)

#Concrete Factory B
class FactoryPrivada:
    @staticmethod
    def criar_mensagem(remetente, conteudo):
        return MensagemPrivada(remetente, conteudo)

#Abstract Factory
class FactoryMensagem(ABC):
    @staticmethod
    def criar_mensagem(tipo, remetente, conteudo):
        if tipo == "grupo":
            return FactoryGrupo.criar_mensagem(remetente, conteudo)
        elif tipo == "privada":
            return FactoryPrivada.criar_mensagem(remetente, conteudo)
        else:
            raise ValueError("Tipo de mensagem desconhecido")