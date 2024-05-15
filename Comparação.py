num = int(input('Digite um número: '))  # Solicita ao usuário que insira o primeiro número
maior = num  # Inicializa a variável 'maior' com o primeiro número inserido
menor = num  # Inicializa a variável 'menor' com o primeiro número inserido
valores = num  # Inicializa a variável 'valores' com o primeiro número inserido
quant = 1  # Inicializa o contador de números inseridos com 1, pois já inserimos o primeiro número

while True:
    num = int(input('Digite um número: '))  # Solicita ao usuário que insira outro número
    valores += num  # Adiciona o número à soma dos valores
    quant += 1  # Incrementa o contador de números inseridos
    média = valores / quant  # Calcula a média dos números inseridos até o momento

    if num > maior:  # Verifica se o número inserido é maior que o atual 'maior'
        maior = num  # Se for maior, atualiza o valor de 'maior'
    elif num < menor:  # Verifica se o número inserido é menor que o atual 'menor'
        menor = num  # Se for menor, atualiza o valor de 'menor'
    
    # Imprime o maior número, o menor número e a média dos números inseridos até o momento
    print('O maior número é', maior)
    print('O menor número é', menor)
    print('A média é', média)  # Imprime a média
