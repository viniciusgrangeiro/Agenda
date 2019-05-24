contato = []
qtdContatos = 0

#MENU AGENDA
continuar = True
while continuar:
    print("=================================================")
    print("=                MINHA AGENDA                   =")
    print("=================================================")
    print("=    1 - Novo Contato                           =")
    print("=    2 - Alterar Contato                        =")
    print("=    3 - Excluir Contato                        =")
    print("=    4 - Listar Todos os Contatos               =")
    print("=    5 - Listar por Codigo do Contato           =")
    print("=    6 - Listar por Nome do Contato             =")
    print("=    7 - Sair                                   =")
    print("=================================================")
    opcao = int(input("Escolha a Opção: "))
    print("=================================================")

    #Opcao 1 - Novo Contato
    if opcao == 1:
        if qtdContatos >= 10:
            print("Limite de Contatos Cadastrados esgotado")
        else:
            print("*************************************************")
            print("Novo Contato")
            print("*************************************************")
            codigo = int(input("Informe o CÓDIGO do Contato: "))
            nome = input("Informe o NOME do Contato: ").upper()
            telefone = input("Informe o TELEFONE do Contato: ")
            if codigo in contato:
                print("*************************************************")
                print(f"Contato com o Codigo {codigo} ja cadastrado.")
                print("*************************************************")
            else:
                contato.append(codigo)
                contato.append(nome)
                contato.append(telefone)
                qtdContatos += 1
                print("*************************************************")
                print(f"Codigo com o CÓDIGO {codigo} cadastrado com sucesso.")
                print("*************************************************")
                print()

    #Opcao 2 - Alterar Contato
    elif opcao == 2:
        print("*************************************************")
        print("Alterar Contato")
        print("*************************************************")
        codigo = int(input("Informe o CÓDIGO do Contato: "))
        if codigo in contato:
            print("*************************************************")
            nome = input("Informe o NOME do Contato: ")
            telefone = input("Informe o TELEFONE do Contato: ")
            print("*************************************************")
            i = contato.index(codigo)
            contato[i+1] = nome
            contato[i+2] = telefone
        else:
            print("*************************************************")
            print(f"Contato com o CÓDIGO {codigo} não cadastrado e não pode ser alterado.")
            print("*************************************************")

    #Opcao 3 - Excluir Contato
    elif opcao == 3:
        print("*************************************************")
        print("Excluir Contato")
        print("*************************************************")
        codigo = int(input("Informe o CÓDIGO do contato: "))
        if codigo in contato:
            i = contato.index(codigo)
            del (contato[i + 2])
            del (contato[i + 1])
            del (contato[i])
            print("*************************************************")
            print(f"Contato com CÓDIGO {codigo} excluido com sucesso.")
            print("*************************************************")
            qtdContatos =- 1
        else:
            print("*************************************************")
            print(f"Contato com o CÓDIGO {codigo} não cadastrado e não pode ser excluído.")
            print("*************************************************")

    #Opcao 4 - Listar Todos os Contatos
    elif opcao == 4:
        print("*************************************************")
        print("Listar Todos os Contatos")
        print("*************************************************")
        if not contato:
            print("Não há contatos cadastrados na Agenda de Contatos.")
        else:
            i = 0
            while i < len(contato):
                print("*************************************************")
                print(f"CÓDIGO do Contato: {contato[i]}")
                i += 1
                print(f"NOME do Contato: {contato[i]}")
                i += 1
                print(f"TELEFONE do Contato: {contato[i]}")
                i += 1
                print("*************************************************")

    #Opcao 5 - Buscar por Código de Contato
    elif opcao == 5:
        print("*************************************************")
        print("Listar por Código de Contato")
        print("*************************************************")
        codigo = int(input("Informe o CÓDIGO do Contato: "))
        print("*************************************************")
        if codigo in contato:
            i = contato.index(codigo)
            print(f"CÓDIGO do Contato: {codigo}")
            print(f"NOME do Contato: {contato[i + 1]}")
            print(f"TELEFONE do Contato : {contato[i + 2]}")
            print("*************************************************")
        else:
            print(f"Contato com o CÓDIGO: {codigo} não cadastrado e não pode ser pesquisado")
            print("*************************************************")

    #Opcao 6 - Buscar por Nome de Contato
    elif opcao == 6:
        print("*************************************************")
        print("Listar por Nome de Contato")
        print("*************************************************")
        nome = input("Informe o NOME do Contato: ").upper()
        if nome in contato:
            i = contato.index(nome)
            print(f"CÓDIGO do Contato: {contato[i-1]}")
            print(f"NOME do Contato: {nome}")
            print(f"TELEFONE do Contato: {contato[i+1]}")
        else:
            print("*************************************************")
            print("fContato com o NOME: {nome} não cadastrado e não pode ser pesquisado")
            print("*************************************************")

    #Opcao 7 - Sair
    elif opcao == 7:
        print("Agenda Encerrada")
        print("=================================================")
        continuar = False


