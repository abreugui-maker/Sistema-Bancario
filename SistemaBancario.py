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
        valor = int(input("Digite o valor a ser depositado:"))
        if valor<=0:
            print("Valor de depósito inválido!")
        else:
            saldo += valor
            extrato['deposito'].append(valor)
            print(f"Depósito de R${valor:0.2f} realizado!", end="\n\n")
    
    elif menu == "2":
        
        
        if saldo == 0 | valor > saldo:
            print("Saldo insuficiente para a operação", f"Seu saldo é {saldo}", end="\n\n")

    elif menu == "3":
        print(extrato)

    elif menu == "4":
        print("Saindo. Tenha um bom dia!")
        break
    else:
        print("Operação inválida")

    print("Selecione uma das uma das operações abaixo:",texto, sep="\n")
