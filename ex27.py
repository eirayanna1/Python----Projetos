prin = []
peso_mais_pesada = 0
pessoa_mais_pesada = ''
peso_mais_leve = float('inf')
pessoa_mais_leve = ''

while True:
    temp = []  # Inicialize a lista temporária dentro do loop
    nome = input('Qual o seu nome? (Digite "sair" para encerrar)').strip().upper()
    
    if nome == "SAIR":
        break
    
    peso = float(input('Qual o seu peso? '))
    temp.append(nome)
    temp.append(peso)
    prin.append(temp[:])
    
    if peso > peso_mais_pesada:
        peso_mais_pesada = peso
        pessoa_mais_pesada = nome
    
    if peso < peso_mais_leve:
        peso_mais_leve = peso
        pessoa_mais_leve = nome

print(f'No total foram cadastradas {len(prin)} pessoas')
print(f'A pessoa mais pesada é {pessoa_mais_pesada} e pesa {peso_mais_pesada} kg')
print(f'A pessoa mais leve é {pessoa_mais_leve} e pesa {peso_mais_leve} kg')
