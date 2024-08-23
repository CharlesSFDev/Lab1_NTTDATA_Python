menu = '''
[d] depositar
[s] sacar
[e]extrato
[q] sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":

        valorDeposito = float(input("Informe o valor que deseja depositar: "))
        
        if valorDeposito > 0:

            saldo = saldo + valorDeposito
            extrato += f"Depósito: R$ {valorDeposito}.\n"

        else:

            print("Insira um valor maior que 0.")

    elif opcao == "s":
        
        valorSaque = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valorSaque > saldo

        excedeu_limite = valorSaque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente para realizar este saque.")
        elif excedeu_limite:
            print("O limite para saque é de R$ 500,00. Insira um valor menor ou igual a este.")
        elif excedeu_saques:
            print("Você já fez o número máximo de saques para o dia de hoje.")
        elif valorSaque > 0:
            saldo = saldo - valorSaque
            numero_saques +=1
            extrato += f"Saque: R$ {valorSaque}.\n"
        else:
            print("Insira um valor maior que 0.")

    elif opcao == "e":
        print("-----EXTRATO-----")
        print(extrato)
        print(f"Saldo: R$ {saldo}.")
        print("-----------------")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

