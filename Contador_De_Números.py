# Inicializa a variável de contagem
contagem = 0

# Loop infinito para receber os números até que 999 seja digitado
while True:
    # Solicita que o usuário digite um número
    num = int(input('Digite números até chegar em 999: '))
    
    # Verifica se o número digitado é 999 para encerrar o loop
    if num == 999:
        break
    # Verifica se o número está fora do intervalo permitido
    elif num < 0 or num > 999:
        print('Valor indisponível!')
    else:
        # Incrementa a contagem se o número estiver no intervalo válido
        contagem += 1

# Exibe o total de números digitados
print('Total de números digitados:', contagem)
