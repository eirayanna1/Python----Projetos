while True:
    num1 = int(input('Digite um número!'))
    num2 = int(input('Digite um número!'))
    num3 = int(input('Digite um número!'))
    num4 = int(input('Digite um número!'))

    # Criando uma tupla com os números digitados
    tupla = (num1, num2, num3, num4)
    
    pares = []  # Inicializando uma lista vazia para armazenar os números pares

    # Iterando sobre os números na tupla para encontrar os pares
    for num in tupla:
        if num % 2 == 0:
            pares.append(num)  # Adicionando o número par à lista pares

    # Imprimindo os valores digitados, a contagem de 9s, a posição do primeiro 3, e os números pares
    print(f'Valores digitados: {tupla}')
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
    if 3 in tupla:
        print(f'O número 3 foi digitado pela primeira vez na posição {tupla.index(3)}')
    else:
        print('O número 3 não foi digitado.')
    print('Os números pares foram:', pares)
