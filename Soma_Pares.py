soma = 0  # Inicializa a variável soma para armazenar a soma dos números pares

# Loop para solicitar ao usuário que insira 6 números
for c in range(6):
    num = int(input("Digite um número: "))  # Solicita ao usuário que insira um número
    if num % 2 == 0:  # Verifica se o número é par
        soma += num  # Se for par, adiciona o número à soma

print(soma)  # Imprime a soma dos números pares
