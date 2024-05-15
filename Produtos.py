total = produtos = 0  # Inicializa variáveis para armazenar o total gasto e o número de produtos
nomeP = ''  # Inicializa uma variável para armazenar o nome do produto mais barato
preçoB = float('inf')  # Inicializa uma variável para armazenar o preço do produto mais barato (começa com infinito)
mais =  0  # Inicializa uma variável para contar quantos produtos custam mais de R$100,00

while True:
    nome = input('Digite o nome do produto: ').strip().upper()  # Solicita o nome do produto
    preço = float(input('Digite o preço do produto: '))  # Solicita o preço do produto
    cont = input('Deseja continuar? S/N: ').strip().upper()  # Pergunta se deseja continuar a inserir produtos

    total += preço  # Atualiza o total gasto somando o preço do produto inserido
    produtos += 1  # Incrementa o contador de produtos

    if preço < preçoB:  # Verifica se o preço do produto atual é menor que o preço do produto mais barato registrado até agora
        nomeP = nome  # Se sim, atualiza o nome do produto mais barato
        preçoB = preço  # Atualiza o preço do produto mais barato

    if preço > 100:  # Verifica se o preço do produto atual é maior que R$100,00
        mais += 1  # Se sim, incrementa o contador de produtos que custam mais de R$100,00

    while cont not in ['S', 'N']:  # Verifica se a resposta para continuar é válida
        cont = input('Por favor, digite S para sim ou N para não: ').strip().upper()  # Solicita novamente a resposta se for inválida

    if cont == 'N':  # Verifica se deseja parar de inserir produtos
        break  # Se sim, encerra o loop

# Após a inserção dos produtos, imprime as estatísticas coletadas
print(f'O total gasto é {total:.2f}')
print(f'O total de produtos é {produtos}')
print(f'O nome do produto mais barato é {nomeP}')
print(f'Quantos produtos custam mais de R$100,00: {mais}')
