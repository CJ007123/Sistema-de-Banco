extrato = []
iniciando_limite = 0
LIMITE_MAXIMO = 3

def depositar(saldo,deposito: float):
    if not isinstance(deposito, float):
        raise TypeError('O depósito precisa ser um número')
    
    if deposito is None:
        raise ValueError('É necessário inserir um valor para o depósito')
    
    if deposito <= 0:
        raise ValueError('Por favor, depósite apenas valores posítivos')

    saldo += deposito 
    valor = f'Valor do depósito R${deposito:.2f}'
    extrato.append(valor)

    return saldo   


def sacar(saldo, saque:float):
    global iniciando_limite

    if not isinstance(saque, float):
        raise TypeError('O saque precisa ser um número')
    
    if saque is None:
        raise ValueError('É necessário inserir um valor para fazer o saque')
    
    if saque <= 0:
        raise ValueError('Por favor, insire um valor posítivo para o saque')
    
    if iniciando_limite >= LIMITE_MAXIMO:
        raise ValueError('O limite de saque chegou ao fim! Volte outro dia para sacar novamente')

    if saldo >= saque:
        saldo -= saque
        iniciando_limite += 1
        valor = f'Valor do saque R${saque:.2f}!' 
        extrato.append(valor)
    else:
        print('O saldo precisa ser maior ou igual ao saque')

    return saldo


def extratos():
    if not extrato:
        print('Não há movimentações aqui')
        return
    for ex in extrato:
        print(ex)
        print()




menu = """
============================
      SISTEMA BANCÁRIO      
============================

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

"""

saldo = 1500.0
while True:
    opcao = int(input(menu))

    try:
        if opcao == 1:
            deposito = float(input('Insira a quantidade que deseja depositar: '))
            saldo = depositar(saldo, deposito)
            print(f'Depósito realizado com sucesso! Valor do depósito R${saldo:.2f}')

        elif opcao == 2:
            sacando = float(input('Insira a valor que deseja sacar: '))   
            saldo = sacar(saldo, sacando) 
            print(f'Saque realizado com sucesso! Valor do saque R${saldo:.2f}')
        
        elif opcao == 3:
            print('Exibindo extrato(s) a seguir:')
            extratos()
            print(f'Saldo atual: {saldo:.2f}\n')
        
        elif opcao == 4:
            print('Finalizando a operação... Obrigado por utilizar o nosso programa!')
            break

        else:
            print('Escolha um número entre 1 a 4.')

    except ValueError as e:
        print(f'Erro: {e}')