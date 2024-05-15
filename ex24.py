lista = []

# Pedindo ao usuário para digitar 5 números e adicionando-os à lista
for _ in range(5):
    lista.append(int(input('Digite um número: ')))

# Encontrando o maior e o menor número na lista
maior = max(lista)
menor = min(lista)

# Imprimindo os números digitados, o maior e o menor número
print(f'Os números digitados foram: {lista}.')
print(f'O maior número digitado foi: {maior}, e o menor número foi: {menor}.')

# Imprimindo os números e suas posições
for posicao, valor in enumerate(lista):
    print(f'O número {valor} está na posição {posicao}.')
