num = int(input('Digite um número: '))  # Solicita ao usuário que insira um número

# Loop para multiplicar o número inserido pelo usuário pelos números de 0 a 10
for c in range(0, 11):
    res = num * c  # Calcula o resultado da multiplicação
    # Imprime a multiplicação formatada como 'num x c = res'
    print('{} x {} = {}'.format(num, c, res))
