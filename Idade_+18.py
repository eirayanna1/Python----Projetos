soma = 0  # Inicializa a variável soma para contar as pessoas maiores de idade

for c in range(7):
    data = int(input('Qual a sua idade? '))  # Solicita a idade do usuário
    if data >= 18:  # Verifica se a idade é maior ou igual a 18
        soma += 1  # Incrementa a contagem de pessoas maiores de idade
    print('Há {} pessoas maiores de idade'.format(soma))
