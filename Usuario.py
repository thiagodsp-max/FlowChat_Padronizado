#Classe própria com elementos

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.logado = False

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            self.logado = True
            return True
        return False

    def logout(self):
        self.logado = False