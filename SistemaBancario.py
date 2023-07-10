# Sistema Bancário

menu = None
texto = '''
Olá, selecione uma das uma das operações abaixo:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
'''
saldo = 0
extrato = ""
limite = 500
numero_saques_dia = 0
LIMITE_SAQUES = 3

print(texto)

while True:

    menu = int(input("Selecione:"))
    
    if menu == 1:
        print("Deposito")
    
    elif menu == 2:
        print("Saque")

    elif menu == 3:
        print("Extrato")

    elif menu == 4:
        print("Saiu")
        break
