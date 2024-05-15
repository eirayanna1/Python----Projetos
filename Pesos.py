
pesos = []  # Lista para armazenar os pesos

# Loop para coletar os pesos de 5 pessoas
for c in range(5):
    peso = int(input('Qual o seu peso? '))  # Solicita o peso da pessoa e converte para inteiro
    pesos.append(peso)  # Adiciona o peso à lista

# Encontra o maior peso usando a função max()
maior = max(pesos)
# Encontra o menor peso usando a função min()
menor = min(pesos)

# Exibe o maior e o menor peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))
