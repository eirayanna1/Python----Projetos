import time  # Importa o módulo time para usar a função sleep

# Loop para a contagem regressiva de 10 a 1
for c in range(10, 0, -1):
    print(c)  # Imprime o número atual da contagem
    time.sleep(1)  # Atraso de 1 segundo entre as iterações
