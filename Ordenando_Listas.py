lista = []

while True:
    numero = int(input('Digite um número: '))
    
    # Verifica se o número já está na lista
    if numero in lista:
        print('Este número já foi adicionado. Por favor, digite outro número.')
    else:
        lista.append(numero)
        per = input('Deseja continuar? Escreva S ou N: ').strip().upper()
        
        # Verifica se o usuário deseja continuar ou não
        if per == 'N':
            break
        elif per != 'S':
            print('Opção inválida. Por favor, digite S para continuar ou N para parar.')

# Ordena a lista em ordem crescente
lista.sort()

# Imprime os valores digitados, agora ordenados
print(f'Você digitou os valores ordenados: {lista}')
