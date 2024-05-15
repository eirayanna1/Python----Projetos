import random

# Lista de itens
lista = ["pedra", "papel", "tesoura"]

# Sortear um item aleatório da lista
item = random.choice(lista)

# Escolha do usuário
escolha = input("Escolha pedra, papel ou tesoura: ")

# Verificação do resultado
if escolha not in lista:
    print('Sua escolha não foi válida!')
elif escolha == item:
    print('O jogo deu empate!')
elif (escolha == "pedra" and item == "tesoura") or (escolha == "papel" and item == "pedra") or (escolha == "tesoura" and item == "papel"):
    print('Minha escolha foi {}, você ganhou'.format(item))
else:
    print('Minha escolha foi {}, você perdeu'.format(item))
