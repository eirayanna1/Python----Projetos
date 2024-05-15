soma = 0  # Inicializa a variável soma

for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print(soma)  # Imprime a soma total
