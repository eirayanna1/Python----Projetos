# Solicita que o usuário escolha dois números
op1 = int(input('Escolha um número: '))
op2 = int(input('Escolha um número: '))

# Loop principal que permite ao usuário escolher entre várias operações
while True:
    # Solicita que o usuário escolha uma opção
    op3 = int(input("""Escolha uma das opções abaixo:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA: """))

    # Verifica a opção escolhida e executa a operação correspondente
    if op3 == 1:
        # Soma os dois números e exibe o resultado
        soma = op1 + op2
        print('A soma entre os valores {} e {} é igual a {}'.format(op1, op2, soma))

    elif op3 == 2:
        # Multiplica os dois números e exibe o resultado
        mul = op1 * op2
        print('A multiplicação entre os valores {} e {} é igual a {}'.format(op1, op2, mul))

    elif op3 == 3:
        # Compara os números e exibe qual é o maior ou se são iguais
        if op1 > op2:
            print('O número {} é maior que o {}'.format(op1, op2))
        elif op1 == op2:
            print('O número {} é igual ao {}'.format(op1, op2))
        else:
            print('O número {} é menor que o {}'.format(op1, op2))

    elif op3 == 4:
        # Permite ao usuário escolher novos números para op1 e op2
        op1 = int(input('Escolha um novo número para op1: '))
        op2 = int(input('Escolha um novo número para op2: '))

    elif op3 == 5:
        # Encerra o programa
        print('Saindo do programa...')
        break

    else:
        # Exibe uma mensagem de erro se a opção escolhida for inválida
        print('Opção inválida. Escolha novamente.')
