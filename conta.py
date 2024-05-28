def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
    else:
        print('Valor inválido')
    return saldo, extrato

def saque(*, saldo, valor, extrato):
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f'Valor sacado: R${valor:.2f}\n'
    else:
        print('Valor de saque inválido ou saldo insuficiente')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('Não foram realizadas transações' if not extrato else extrato)
    print(f'Saldo atual: R${saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário com esse CPF')
        return
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereço (Logradouro, número - bairro - cidade/sigla estado): ')

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    })

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Insira o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    else:
        print('Usuário não encontrado. Crie um usuário primeiro.')
        return None

def menu():
    try:
        opcao = int(input("""======= MENU =======
1) Depositar
2) Sacar
3) Extrato
4) Cadastrar usuário
5) Criar Conta
0) Sair
--------------------
Digite a opção desejada: """))
        return opcao
    except ValueError:
        print("Opção inválida! Digite um número.")
        return -1

def main():
    saldo = 0
    limite_saques = 0
    extrato = ''
    usuarios = []
    contas = []
    agencia = '001'
    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input('Digite o valor a ser depositado: '))
            saldo, extrato = deposito(saldo, valor, extrato)
            print(f'Foi depositado na sua conta R${valor:.2f} e o saldo é de R${saldo:.2f}')
        
        elif opcao == 2:
            valor = float(input('Digite o valor que deseja sacar: '))
            if limite_saques < 3:
                if valor <= 500:
                    if valor <= saldo:
                        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato)
                        print(f'Saque de R${valor:.2f} realizado com sucesso!')
                        limite_saques += 1
                    else:
                        print('Saldo insuficiente para o saque.')
                else:
                    print('Valor de saque maior que o permitido.')
            else:
                print('Quantidade de saques excedida.')
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)
            print('Usuário criado com sucesso.')
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                print('Conta criada com sucesso.')
        
        elif opcao == 0:
            print('Saindo...')
            break
        
        else:
            print('Opção inválida. Tente novamente.')

main()
