from abc import ABC, abstractmethod

class PesquisaStrategy(ABC):
    @abstractmethod
    def pesquisar(self, mensagens, termo):
        pass

class PesquisaParcial(PesquisaStrategy):

    def pesquisar(self, mensagens, termo):
        return [
            mensagem
            for mensagem in mensagens
            if termo.lower() in mensagem.conteudo.lower()
        ]
    
class PesquisaExata(PesquisaStrategy):

    def pesquisar(self, mensagens, termo):
        return [
            mensagem
            for mensagem in mensagens
            if mensagem.conteudo.lower() == termo.lower()
        ]
    
class PesquisaPorRemetente(PesquisaStrategy):

    def pesquisar(self, mensagens, termo):

        return [
            mensagem
            for mensagem in mensagens
            if termo.lower()
            in mensagem.remetente.email.lower()
        ]
    
