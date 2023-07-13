import textwrap

def menu():
    menu = """\n
    ============ MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n === Depósito realizado com sucesso! ===")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso!! ===")

    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def gerar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuario com este CPF!")
        return
    
    nome = input("\nInforme nome completo: ")
    data_nascimento = input("\nInforme data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme endereco (logradouro, num - Bairro - Cidade/Estado): ")

    usuarios.append({'nome':nome, 'data_nascimento': data_nascimento, 'cpf':cpf, 'endereco': endereco})

    print("\n=== Usuario criado com sucesso!! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_contacorrente(agencia, numero_conta, usuarios):
    cpf = input("\nInforme o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso!! ===")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print("\nUsuario não encontrado! Fluxo de criação de conta encerrado!")
    
def listar_contas(contas):
    if contas:
        print("\n==== Lista de Contas ====")
        for index, conta in enumerate(contas):
            print(f"\nConta {index}:")
            print(f"\tAgencia: {conta['agencia']}")
            print(f"\tNumero da conta: {conta['numero_conta']}")
            print(f"\tNome: {conta['usuario']['nome']}, Data Nascimento: {conta['usuario']['data_nascimento']}, CPF: {conta['usuario']['cpf']}")
            print(f"\tEndereco: {conta['usuario']['endereco']}")

        print("\n", "="*30)
    else:
        print("\nErro! Não há lista de contas!")

def main():
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(saldo=saldo,
                                    valor=valor,
                                    extrato=extrato,
                                    limite=limite,
                                    numero_saques=numero_saques,
                                    limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            gerar_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_contacorrente(NUMERO_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()