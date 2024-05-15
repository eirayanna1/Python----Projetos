import random  # Importa o módulo random para gerar números aleatórios

c = 0  # Inicializa o contador de escolhas do usuário

while True:
    num_usuario = int(input('Escolha um número: '))  # Solicita ao usuário que escolha um número
    per = input('Escolha entre par ou ímpar: ').strip().lower()  # Solicita ao usuário que escolha par ou ímpar
    
    num_computador = random.randint(0, 10)  # Gera aleatoriamente um número para o computador
    
    soma = num_usuario + num_computador  # Calcula a soma dos números escolhidos pelo usuário e pelo computador

    if soma % 2 == 0 and per == "par":  # Verifica se a soma é par e se o usuário escolheu par
        print('Parabéns! Você venceu!')  # Se sim, imprime que o usuário venceu
        c += 1  # Incrementa o contador de escolhas
        print(f'Você fez {c} escolhas!')  # Imprime o número de escolhas do usuário
        break  # Encerra o loop
    elif soma % 2 != 0 and per == "ímpar":  # Verifica se a soma é ímpar e se o usuário escolheu ímpar
        print('Parabéns! Você venceu!')  # Se sim, imprime que o usuário venceu
        print(f'O computador escolheu {num_computador}')  # Imprime o número escolhido pelo computador
        c += 1  # Incrementa o contador de escolhas
        print(f'Você fez {c} escolhas!')  # Imprime o número de escolhas do usuário
        break  # Encerra o loop
    else:
        print('Você perdeu! Tente novamente!')  # Se não, imprime que o usuário perdeu e solicita uma nova tentativa
        print(f'O computador escolheu {num_computador}')  # Imprime o número escolhido pelo computador
