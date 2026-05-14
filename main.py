from FlowChat import FlowChat
from ChatIndividual import ChatIndividual
from Grupo import Grupo

import os


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_mensagens(chat):
    chat.remover_mensagens_expiradas()

    if len(chat.mensagens) == 0:
        print("Nenhuma mensagem ainda.\n")
        return

    for i, mensagem in enumerate(chat.mensagens, start=1):
        mensagem.exibir(i)


def mostrar_cabecalho_chat(chat, usuario):
    if isinstance(chat, ChatIndividual):
        print(f"{chat.titulo(usuario)}\n")
    elif isinstance(chat, Grupo):
        print(f"{chat.titulo()}\n")
        print("Membros:")
        for membro in chat.membros:
            print(f"- {membro.email}")
        print()


def menu_login(sistema):
    while sistema.usuario_logado is None:
        print("\n********** Bem vindo ao FlowChat! **********")
        print("1- Login")
        print("2- Cadastro")
        print("0- Sair")

        try:
            opcao = int(input("\n"))

            if opcao == 0:
                return False

            elif opcao == 1:
                limpar_terminal()
                email = input("Digite seu Email: ")
                senha = input("Digite sua senha: ")

                if sistema.login(email, senha):
                    limpar_terminal()
                    print(f"Bem vindo, {sistema.usuario_logado.email}!")
                else:
                    limpar_terminal()
                    print("Falha no login.")

            elif opcao == 2:
                limpar_terminal()
                email = input("Digite seu Email: ")
                senha = input("Digite sua senha: ")

                if sistema.cadastrar_usuario(email, senha):
                    limpar_terminal()
                    print("Cadastro realizado com sucesso!")
                else:
                    limpar_terminal()
                    print("Já existe um usuário cadastrado com esse email!")

            else:
                limpar_terminal()
                print("Opção inválida.")

        except ValueError:
            limpar_terminal()
            print("Opção inválida.")

    return True


def menu_principal(sistema):
    usuario = sistema.usuario_logado
    total_mencoes = sistema.total_notificacoes_grupos(usuario)

    print("1- Ver Chats Individuais")
    print("2- Criar Novo Chat Individual")
    if total_mencoes > 0:
        print(f"3- Ver Grupos ({total_mencoes})")
    else:
        print("3- Ver Grupos")
    print("4- Criar Novo Grupo")
    print("0- Deslogar")

    try:
        opcao = int(input("\n"))

        if opcao == 0:
            sistema.logout()
            limpar_terminal()
            return

        elif opcao == 1:
            limpar_terminal()
            chats = sistema.chats_do_usuario(usuario)

            print("Chats Individuais:\n")

            if len(chats) == 0:
                print("Você não possui chats individuais.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            for i, chat in enumerate(chats, start=1):
                print(f"{i} - Chat com {chat.outro_usuario(usuario).email}")

            try:
                escolha = int(input("\nEscolha um chat para abrir (0 para voltar): "))

                if escolha == 0:
                    limpar_terminal()
                    return

                if escolha < 1 or escolha > len(chats):
                    limpar_terminal()
                    print("Opção inválida.")
                    return

                chat = chats[escolha - 1]
                chat.abrir_chat()
                sistema.chat_aberto = chat
                limpar_terminal()

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

        elif opcao == 2:
            limpar_terminal()
            print("Criar Novo Chat Individual:\n")

            email_destino = input("Digite o email do usuário: ").strip()
            usuario_destino = sistema.buscar_usuario_por_email(email_destino)

            if usuario_destino is None:
                print("\nUsuário não encontrado.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            if usuario_destino == usuario:
                print("\nVocê não pode iniciar um chat com você mesmo.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            sistema.criar_ou_abrir_chat_individual(usuario_destino)
            limpar_terminal()

        elif opcao == 3:
            limpar_terminal()
            grupos = sistema.grupos_do_usuario(usuario)

            print("Grupos:\n")

            if len(grupos) == 0:
                print("Você não participa de nenhum grupo.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            for i, grupo in enumerate(grupos, start=1):
                qtd = grupo.qtd_notificacoes(usuario)
                if qtd > 0:
                    print(f"{i} - {grupo.nome} ({qtd})")
                else:
                    print(f"{i} - {grupo.nome}")

            try:
                escolha = int(input("\nEscolha um grupo para abrir (0 para voltar): "))

                if escolha == 0:
                    limpar_terminal()
                    return

                if escolha < 1 or escolha > len(grupos):
                    limpar_terminal()
                    print("Opção inválida.")
                    return

                grupo = grupos[escolha - 1]
                grupo.limpar_notificacoes(usuario)
                sistema.chat_aberto = grupo
                limpar_terminal()

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

        elif opcao == 4:
            limpar_terminal()
            print("Criar Grupo:\n")

            nome_grupo = input("Digite o nome do grupo: ").strip()

            if nome_grupo == "":
                print("\nO nome do grupo não pode ser vazio.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            for grupo in sistema.grupos:
                if grupo.nome and grupo.nome.lower() == nome_grupo.lower():
                    print("\nJá existe um grupo com esse nome.")
                    input("\nPressione Enter para continuar...")
                    limpar_terminal()
                    return

            print("\nDigite os emails dos participantes separados por vírgula.")
            print("Exemplo: a@gmail.com, b@gmail.com, c@gmail.com\n")

            entrada = input("Emails: ").strip()
            emails = []

            if entrada != "":
                emails = [email.strip() for email in entrada.split(",") if email.strip() != ""]

            grupo = sistema.criar_grupo(nome_grupo, emails)

            if grupo is None:
                print("\nUm ou mais emails não foram encontrados.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            print(f"\nGrupo '{nome_grupo}' criado com sucesso.")
            input("\nPressione Enter para continuar...")
            limpar_terminal()

        else:
            limpar_terminal()
            print("Opção inválida.")

    except ValueError:
        limpar_terminal()
        print("Opção inválida.")


def menu_enquete(chat, usuario):
    limpar_terminal()

    if len(chat.enquetes) == 0:
        print("Não há enquetes neste chat.")
        input("\nPressione Enter para continuar...")
        limpar_terminal()
        return

    for i, enquete in enumerate(chat.enquetes, start=1):
        print(f"{i} - {enquete.pergunta}")

    try:
        indice = int(input("\nEscolha uma enquete (0 para voltar): "))

        if indice == 0:
            limpar_terminal()
            return

        if indice < 1 or indice > len(chat.enquetes):
            limpar_terminal()
            print("Enquete inválida.")
            return

        enquete = chat.enquetes[indice - 1]

        while True:
            limpar_terminal()
            print(f"Enquete: {enquete.pergunta}\n")

            if len(enquete.votos) == 0:
                print("Nenhum voto ainda.")
            else:
                print("Votos atuais:")
                for email, voto in enquete.votos.items():
                    print(f"{email}: {voto}")

            print("\n1- Votar")
            print("2- Ver resultado")
            print("0- Voltar")

            try:
                acao = int(input("\n"))

                if acao == 0:
                    limpar_terminal()
                    return

                elif acao == 1:
                    voto = input("\nDigite seu voto: ").strip()

                    if voto == "":
                        print("\nO voto não pode ser vazio.")
                        input("\nPressione Enter para continuar...")
                        continue

                    enquete.votar(usuario, voto)
                    print("\nVoto registrado com sucesso.")
                    input("\nPressione Enter para continuar...")

                elif acao == 2:
                    limpar_terminal()
                    print(f"Resultado da enquete: {enquete.pergunta}\n")

                    if len(enquete.votos) == 0:
                        print("Nenhum voto registrado.")
                    else:
                        for email, voto in enquete.votos.items():
                            print(f"{email}: {voto}")

                    input("\nPressione Enter para continuar...")

                else:
                    limpar_terminal()
                    print("Opção inválida.")

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

    except ValueError:
        limpar_terminal()
        print("Opção inválida.")


def menu_eventos(chat, usuario):
    limpar_terminal()

    if len(chat.eventos) == 0:
        print("Não há eventos neste chat.")
        input("\nPressione Enter para continuar...")
        limpar_terminal()
        return

    for i, evento in enumerate(chat.eventos, start=1):
        print(f"{i} - {evento.nome} | {evento.data} | {evento.status}")

    try:
        indice = int(input("\nEscolha um evento (0 para voltar): "))

        if indice == 0:
            limpar_terminal()
            return

        if indice < 1 or indice > len(chat.eventos):
            limpar_terminal()
            print("Evento inválido.")
            return

        evento = chat.eventos[indice - 1]

        while True:
            limpar_terminal()
            print(f"Evento: {evento.nome}")
            print(f"Data: {evento.data}")
            print(f"Organizador: {evento.organizador.email}")
            print(f"Descrição: {evento.descricao}")
            print(f"Status: {evento.status}\n")

            if evento.organizador == usuario:
                print("1- Editar Evento")
                print("2- Cancelar Evento")
                print("0- Voltar")
            else:
                print("0- Voltar")

            try:
                acao = int(input("\n"))

                if acao == 0:
                    limpar_terminal()
                    return

                if evento.organizador != usuario:
                    limpar_terminal()
                    print("Apenas o organizador pode editar este evento.")
                    input("\nPressione Enter para continuar...")
                    continue

                if acao == 1:
                    novo_nome = input("\nNovo nome do evento (Enter para manter): ").strip()
                    nova_data = input("Nova data do evento (Enter para manter): ").strip()
                    nova_descricao = input("Nova descrição do evento (Enter para manter): ").strip()
                    novo_status = input("Novo status do evento (Enter para manter): ").strip()

                    evento.editar(
                        usuario,
                        nome=novo_nome if novo_nome != "" else None,
                        data=nova_data if nova_data != "" else None,
                        descricao=nova_descricao if nova_descricao != "" else None,
                        status=novo_status if novo_status != "" else None,
                    )

                    print("\nEvento editado com sucesso.")
                    input("\nPressione Enter para continuar...")

                elif acao == 2:
                    evento.cancelar(usuario)
                    print("\nEvento cancelado com sucesso.")
                    input("\nPressione Enter para continuar...")

                else:
                    limpar_terminal()
                    print("Opção inválida.")

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

    except ValueError:
        limpar_terminal()
        print("Opção inválida.")


def menu_chat(sistema):
    chat = sistema.chat_aberto
    usuario = sistema.usuario_logado

    chat.remover_mensagens_expiradas()

    limpar_terminal()
    mostrar_cabecalho_chat(chat, usuario)
    mostrar_mensagens(chat)

    print("\n1- Enviar Mensagem")
    print("2- Pesquisar")
    print("3- Fixar Mensagem")
    print("4- Mensagem Temporária")
    print("5- Criar Enquete")
    print("6- Ver/Votar Enquete")
    print("7- Reagir a Mensagem")
    print("8- Criar Evento")
    print("9- Ver Eventos")
    print("0- Fechar chat")

    try:
        opcao = int(input("\n"))

        if opcao == 0:
            if isinstance(chat, ChatIndividual):
                chat.fechar_chat()
            sistema.chat_aberto = None
            limpar_terminal()
            return

        elif opcao == 1:
            conteudo = input("\nDigite a mensagem: ").strip()

            if conteudo == "":
                limpar_terminal()
                print("Mensagem vazia.")
                return

            if isinstance(chat, Grupo):
                chat.registrar_mensagem(usuario, conteudo)
            else:
                mensagem = chat.criar_mensagem(usuario, conteudo)
                chat.enviar_mensagem(mensagem)

            input("\nPressione Enter para continuar...")
            limpar_terminal()

        elif opcao == 2:
            termo = input("\nDigite o termo de pesquisa: ").strip()

            limpar_terminal()
            print(f"Resultados da pesquisa por: {termo}\n")

            resultados = chat.pesquisar_mensagens(termo)

            if len(resultados) == 0:
                print("Nenhuma mensagem encontrada.")
            else:
                for i, mensagem in enumerate(resultados, start=1):
                    mensagem.exibir(i)

            input("\nPressione Enter para continuar...")
            limpar_terminal()

        elif opcao == 3:
            if len(chat.mensagens) == 0:
                print("\nNão há mensagens para fixar.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            try:
                indice = int(input("\nDigite o número da mensagem que deseja fixar: "))

                if chat.fixar_mensagem(indice):
                    print("\nMensagem fixada com sucesso.")
                else:
                    print("\nMensagem inválida.")

                input("\nPressione Enter para continuar...")
                limpar_terminal()

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

        elif opcao == 4:
            conteudo = input("\nDigite a mensagem temporária: ").strip()

            if conteudo == "":
                limpar_terminal()
                print("Mensagem vazia.")
                return

            mensagem = chat.criar_mensagem(usuario, conteudo)
            chat.enviar_mensagem_temporaria(mensagem, 5)

            if isinstance(chat, Grupo) and "@todos" in conteudo:
                chat.mencionar_todos(usuario)

            print("\nMensagem temporária enviada. Ela será apagada em 5 segundos.")
            input("\nPressione Enter para continuar...")
            limpar_terminal()

        elif opcao == 5:
            pergunta = input("\nDigite a pergunta da enquete: ").strip()

            if pergunta == "":
                limpar_terminal()
                print("A pergunta não pode ser vazia.")
                return

            chat.criar_enquete(pergunta)
            print("\nEnquete criada com sucesso.")
            input("\nPressione Enter para continuar...")
            limpar_terminal()

        elif opcao == 6:
            menu_enquete(chat, usuario)

        elif opcao == 7:
            if len(chat.mensagens) == 0:
                print("\nNão há mensagens para reagir.")
                input("\nPressione Enter para continuar...")
                limpar_terminal()
                return

            try:
                indice = int(input("\nDigite o número da mensagem: "))

                print("\nEscolha uma reação:")
                print("1- 👍")
                print("2- 👎")
                print("3- ❤️")
                print("4- 😺")

                opcao_reacao = int(input("\n"))

                if opcao_reacao == 1:
                    reacao = "👍"
                elif opcao_reacao == 2:
                    reacao = "👎"
                elif opcao_reacao == 3:
                    reacao = "❤️"
                elif opcao_reacao == 4:
                    reacao = "😺"
                else:
                    limpar_terminal()
                    print("Reação inválida.")
                    return

                if chat.reagir_mensagem(indice, reacao):
                    print("\nReação adicionada com sucesso.")
                else:
                    print("\nMensagem inválida.")

                input("\nPressione Enter para continuar...")
                limpar_terminal()

            except ValueError:
                limpar_terminal()
                print("Opção inválida.")

        elif opcao == 8:
            nome = input("\nDigite o nome do evento: ").strip()
            data = input("Digite a data do evento: ").strip()
            descricao = input("Digite a descrição do evento: ").strip()

            if nome == "" or data == "" or descricao == "":
                limpar_terminal()
                print("Todos os campos do evento devem ser preenchidos.")
                return

            chat.criar_evento(nome, data, usuario, descricao)
            print("\nEvento criado com sucesso.")
            input("\nPressione Enter para continuar...")
            limpar_terminal()

        elif opcao == 9:
            menu_eventos(chat, usuario)

        else:
            limpar_terminal()
            print("Opção inválida.")

    except ValueError:
        limpar_terminal()
        print("Opção inválida.")


def main():
    sistema = FlowChat()

    while True:
        if sistema.usuario_logado is None:
            continuar = menu_login(sistema)
            if not continuar:
                break
        elif sistema.chat_aberto is None:
            menu_principal(sistema)
        else:
            menu_chat(sistema)


if __name__ == "__main__":
    main()