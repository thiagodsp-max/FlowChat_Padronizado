#
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

#Abstração da mensagem
class Mensagem:
    def __init__(self, remetente, conteudo, leitura):
        self.remetente = remetente
        self.conteudo = conteudo

        self.reacoes = []
        self.fixada = False
        self.expira_em = None

        self.leitura = leitura
    def marcar_como_lida(self, usuario=None):
        self.leitura.marcar_como_lida(usuario)
    def add_reacao(self, reacao):
        self.reacoes.append(reacao)
    def fixar_mensagem(self):
        self.fixada = True
    
    def obter_status_leitura(self):
        return self.leitura.obter_status()
    #Método importante
    def exibir(self, indice=None):
        prefixo = (f"{indice} - " if indice is not None else "")
        print(
            f"{prefixo}"
            f"{self.remetente.email}: "
            f"{self.conteudo}"
        )
    def expirou(self):
        return (self.expira_em is not None
        and datetime.now() >= self.expira_em)

    def definir_tempo_expiracao(self, segundos):
        self.expira_em = datetime.now() + timedelta(seconds=segundos)


#Implementação Abstrata
class LeituraMensagem(ABC):
    @abstractmethod
    def marcar_como_lida(self, usuario=None):
        pass
    @abstractmethod
    def obter_status(self):
        pass

#Implementações concretas
class LeituraMensagemPrivada(LeituraMensagem):
    def __init__(self):
        self.visualizada = False

    def marcar_como_lida(self, usuario=None):
        self.visualizada = True
    
    def obter_status(self):
        return self.visualizada

class LeituraMensagemGrupo(LeituraMensagem):
    def __init__(self):
        self.lida_por=[]

    def marcar_como_lida(self, usuario=None):
        # Lógica para marcar como lida em um chat de grupo, considerando o usuário
        if usuario.email not in self.lida_por:
            self.lida_por.append(usuario.email)
    def obter_status(self):
        return self.lida_por
