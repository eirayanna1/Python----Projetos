import random  # Importa o módulo random para gerar números aleatórios

# Gera um número aleatório entre 0 e 5
num = random.randint(0, 5)

# Loop para permitir múltiplas tentativas
while True:
    # Solicita ao usuário que escolha um número entre 0 e 5
    txt = int(input("Escolha um número entre 0 e 5: "))

    # Verifica se o número escolhido pelo usuário é igual ao número gerado aleatoriamente
    if txt == num:
        print("Parabéns, você acertou!")
        break  # Encerra o loop se o usuário acertar
    else:
        print("Tente novamente! Eu escolhi o número {} e não o {}".format(num, txt))
