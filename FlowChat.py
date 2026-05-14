from ChatIndividual import ChatIndividual
from Grupo import Grupo

#Sistema de Interno que define o funcionamento do Aplicativo
#enquanto o programa estiver rodando, a classe responsável por 
#manter o estado do sistema, como usuários, grupos e chats individuais
#é uma memória mais do tipo cache, do que um armazenamento interno duradouro

class FlowChat:
    def __init__(self):
        self.usuarios = []
        self.grupos = []
        self.chats_individuais = []
        self.usuario_logado = None
        self.chat_aberto = None

    def cadastrar_usuario(self, email, senha):
        if self.buscar_usuario_por_email(email) is not None:
            return False

        from Usuario import Usuario
        self.usuarios.append(Usuario(email, senha))
        return True

    def buscar_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def login(self, email, senha):
        usuario = self.buscar_usuario_por_email(email)
        if usuario and usuario.login(email, senha):
            self.usuario_logado = usuario
            return True
        return False

    def logout(self):
        if self.usuario_logado:
            self.usuario_logado.logout()
        self.usuario_logado = None
        self.chat_aberto = None

    def buscar_chat_individual(self, usuario1, usuario2):
        for chat in self.chats_individuais:
            if (chat.usuario1 == usuario1 and chat.usuario2 == usuario2) or (chat.usuario1 == usuario2 and chat.usuario2 == usuario1):
                return chat
        return None

    def criar_ou_abrir_chat_individual(self, usuario_destino):
        chat = self.buscar_chat_individual(self.usuario_logado, usuario_destino)

        if chat is None:
            chat = ChatIndividual(self.usuario_logado, usuario_destino)
            self.chats_individuais.append(chat)

        chat.abrir_chat()
        self.chat_aberto = chat
        return chat

    def chats_do_usuario(self, usuario):
        return [chat for chat in self.chats_individuais if chat.usuario1 == usuario or chat.usuario2 == usuario]

    def criar_grupo(self, nome, emails):
        grupo = Grupo(nome)
        grupo.add_membro(self.usuario_logado)

        for email in emails:
            usuario = self.buscar_usuario_por_email(email)
            if usuario is None:
                return None
            grupo.add_membro(usuario)

        self.grupos.append(grupo)
        return grupo

    def grupos_do_usuario(self, usuario):
        return [grupo for grupo in self.grupos if usuario in grupo.membros]

    def total_notificacoes_grupos(self, usuario):
        return sum(grupo.qtd_notificacoes(usuario) for grupo in self.grupos_do_usuario(usuario))