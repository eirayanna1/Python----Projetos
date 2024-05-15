import random

# Gerar uma lista de 5 números inteiros aleatórios
c = [random.randint(0, 100) for _ in range(5)]

# Inicializar maior e menor com o primeiro elemento da lista c
maior = c[0]
menor = c[0]

# Percorrer todos os números na lista c para encontrar o maior e o menor
for num in c:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'Os números gerados foram {c}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
