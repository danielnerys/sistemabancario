# definindo variaveis de controle fora do laço de repetição
saldo = 5000
saque_diarios = 0
extrato = ""

# Iniciando repetição para controle
while True:
    opcao = int(input("""=======Olá======
1) Depositar
2) Sacar
3) Extrato
0) Sair
---------Digite a opção desejada---------- \n Opção: """))

# Criando opção de deposito
    if opcao == 1:
        deposito = input('Digite o valor que deseja depositar: ')
        deposito = float(deposito)
        saldo += int(deposito)
        extrato += f'Depositado: {deposito} '
        print(f'o valor depositado foi de {deposito}')
    else:
        pass

# Criando opção de saque
    if opcao == 2:
        if saque_diarios < 3:
            saque = input('Digite o valor de saque:')
            saque = float(saque)
            if int(saque) > saldo:
                print('Saldo indisponivel para saque')
            elif saque > 500:
                print('O limite de saque é de R$500')
            else:
                saldo -= saque
                extrato += f'Sacado: {saque} '
                print(f'Você sacou {saque} e seu saldo agora é de {saldo}')
                saque_diarios += 1

        else:
            print('Saques diários excedidos, volte novamente amanhã.')
# Opção de exibir extrato
    if opcao == 3:
        print(f"------Extrato bancário-------- \n {extrato}")
    else:
        pass
# Opção para encerrar o menu    
    if opcao == 0:
        print('Obrigado por utilizar nossos serviços!')
        break
