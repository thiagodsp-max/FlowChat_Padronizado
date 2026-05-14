#Classe para as Enquentes

class Enquete:
    def __init__(self, pergunta):
        self.pergunta = pergunta
        self.votos = {}

    def votar(self, usuario, opcao):
        self.votos[usuario.email] = opcao

    def exibir_resultado(self):
        return self.votos