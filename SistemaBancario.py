# Sistema Bancário

menu = None
texto = '''
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
'''
saldo = 0
extrato = {'deposito':[], 'saque':[]}
limite = 500
numero_saques_dia = 0
LIMITE_SAQUES = 3

print("Olá, Bem Vindo ao Banco X!","Selecione uma das uma das operações abaixo:",texto, sep="\n")

while True:

    menu = str(input("Selecione:"))
    
    if menu == "1":
        valor = float(input("Digite o valor a ser depositado:"))
        if valor<=0:
            print("Valor de depósito inválido!")
        else:
            saldo += valor
            extrato['deposito'].append(valor)
            print(f"Depósito de R${valor:.2f} realizado!", end="\n\n")
    
    elif menu == "2":
        if numero_saques_dia < LIMITE_SAQUES:
            numero_saques_dia += 1
            valor = float(input("Digite o valor a ser sacado:"))
        
            if valor>500:
                print("Não foi possível, pois seu limite de saque é de R$500.00.")
            elif valor<=0:
                print("Valor de saque inválido!")
            elif saldo == 0 or valor > saldo:
                print("Saldo insuficiente para a operação")
                print(f"Seu saldo é R${saldo:.2f}", end="\n\n")
            else:
                saldo -= valor
                extrato['saque'].append(valor)
                print(f"Saque de R${valor:.2f} realizado!", end="\n\n")
        else:
            print("Você já atingiu seu máximo número de saques diário!")

    elif menu == "3":
        print("EXTRATO BANCÁRIO", "---------------", sep="\n")

        for k, v in extrato.items():
            for i in v:
                print(f"{k.title()}:       R${i:.2f}")

        print("---------------")
        print(f"Saldo:       R${saldo:.2f}",end="\n\n")

    elif menu == "4":
        print("Tchau. Volte sempre!")
        break
    else:
        print("Operação inválida")

    print("Selecione uma das uma das operações abaixo:",texto, sep="\n")
