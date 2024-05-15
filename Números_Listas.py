prin = []  # Lista principal para armazenar todas as entradas
pares = []  # Lista para armazenar números pares
ímpares = []  # Lista para armazenar números ímpares

while True:
    num = int(input('Digite um número: '))
    prin.append(num)  # Adiciona o número à lista principal

    if num % 2 == 0:
        pares.append(num)  # Se o número for par, adiciona à lista de pares
    else:
        ímpares.append(num)  # Se o número for ímpar, adiciona à lista de ímpares

    cont = input('Deseja continuar? (S / N): ').upper().strip()
    if cont != 'S':
        break

print(f'Números digitados: {prin}')  # Imprime todos os números digitados
print(f'Números pares: {pares}')  # Imprime os números pares
print(f'Números ímpares: {ímpares}')  # Imprime os números ímpares
