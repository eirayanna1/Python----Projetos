lista = []

# Inicializa uma lista vazia para armazenar os números fornecidos pelo usuário.

for _ in range(5):
    # Solicita ao usuário para digitar 5 números e os adiciona à lista.
    lista.append(int(input('Digite um número: ')))

# Usa a função max() para encontrar o maior número na lista e min() para encontrar o menor.
maior = max(lista)
menor = min(lista)

# Imprime os números digitados, o maior e o menor número.
print(f'Os números digitados foram: {lista}.')
print(f'O maior número digitado foi: {maior}, e o menor número foi: {menor}.')

# Itera sobre a lista usando a função enumerate() para imprimir cada número com sua posição na lista.
for posicao, valor in enumerate(lista):
    print(f'O número {valor} está na posição {posicao}.')
