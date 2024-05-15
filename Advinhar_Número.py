import random  # Importa o módulo random para gerar números aleatórios
from time import sleep  # Importa a função sleep do módulo time para pausar o programa

com = random.randint(0, 10)  # Escolhe aleatoriamente um número entre 0 e 10 para o computador
palpites = 0  # Inicializa o contador de palpites

# Loop para o jogador fazer palpites até acertar o número escolhido pelo computador
while True:
    num = int(input('Escolha um número entre 0 e 10: '))  # Solicita ao jogador que escolha um número
    palpites += 1  # Incrementa o contador de palpites a cada tentativa

    if num < 0 or num > 10:  # Verifica se o número está dentro do intervalo válido
        print('Tente novamente entre os números 0 e 10')
    elif num == com:  # Verifica se o número escolhido pelo jogador é igual ao número escolhido pelo computador
        sleep(1)  # Pausa o programa por 1 segundo antes de imprimir a mensagem
        print('Você acertou! O número escolhido foi', com)  # Imprime uma mensagem de acerto
        break  # Encerra o loop, pois o jogador acertou
    else:
        print('Você errou! Tente novamente.')  # Se o jogador errar, imprime uma mensagem de erro

# Imprime o número de palpites que o jogador fez para vencer o jogo
print('Você deu {} palpites para vencer o jogo!'.format(palpites))
