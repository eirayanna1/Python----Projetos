lista = []

while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Este número já foi adicionado. Por favor, digite outro número.')
    else:
        lista.append(numero)
        per = input('Deseja continuar? Escreva S ou N: ').strip().upper()
        if per == 'N':
            break
        elif per != 'S':
            print('Opção inválida. Por favor, digite S para continuar ou N para parar.')

lista.sort()  # Ordenando a lista

print(f'Você digitou os valores ordenados: {lista}')
