# Inicialize uma lista vazia para armazenar os dados das pessoas
prin = []

# Inicialize variáveis para acompanhar a pessoa mais pesada e mais leve
peso_mais_pesada = 0
pessoa_mais_pesada = ''
peso_mais_leve = float('inf')
pessoa_mais_leve = ''

# Inicie um loop infinito para receber dados das pessoas
while True:
    # Inicialize uma lista temporária dentro do loop para armazenar os dados temporários
    temp = []
    
    # Pergunte o nome da pessoa. Digitar "sair" encerra o loop.
    nome = input('Qual o seu nome? (Digite "sair" para encerrar)').strip().upper()
    
    if nome == "SAIR":
        break
    
    # Pergunte o peso da pessoa
    peso = float(input('Qual o seu peso? '))
    
    # Adicione o nome e peso da pessoa à lista temporária
    temp.append(nome)
    temp.append(peso)
    
    # Adicione a lista temporária à lista principal
    prin.append(temp[:])
    
    # Atualize a pessoa mais pesada, se aplicável
    if peso > peso_mais_pesada:
        peso_mais_pesada = peso
        pessoa_mais_pesada = nome
    
    # Atualize a pessoa mais leve, se aplicável
    if peso < peso_mais_leve:
        peso_mais_leve = peso
        pessoa_mais_leve = nome

# Após sair do loop, imprima algumas estatísticas
print(f'No total foram cadastradas {len(prin)} pessoas')
print(f'A pessoa mais pesada é {pessoa_mais_pesada} e pesa {peso_mais_pesada} kg')
print(f'A pessoa mais leve é {pessoa_mais_leve} e pesa {peso_mais_leve} kg')

