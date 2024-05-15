# Criando listas vazias para armazenar os números, pares e ímpares
lista = []
listPar = []
listImp = []

# Loop infinito
while True:
    # Pedindo ao usuário para digitar um número e adicionando à lista
    numero = int(input('Digite um número: '))  # Salvar o número digitado
    lista.append(numero)
    
    # Perguntando ao usuário se ele quer continuar
    cont = input('Você quer continuar? (S / N): ').strip().upper()
    
    # Verificando a entrada do usuário
    while cont not in ['S', 'N']:  # Enquanto não for 'S' ou 'N', pedir novamente
        print('Escolha S ou N')
        cont = input('Você quer continuar? (S / N): ').strip().upper()

    if cont == 'N':  # Se o usuário digitar 'N', encerramos o loop
        break

# Verificando os números para pares e ímpares
for numero in lista:
    if numero % 2 == 0:  # Se o número for par
        listPar.append(numero)  # Adicionar à lista de pares
    else:
        listImp.append(numero)  # Se não, adicionar à lista de ímpares

# Imprimindo as listas
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {listPar}')
print(f'Os números ímpares digitados foram: {listImp}')
