
# Solicita que o usuário digite seu nome e remove espaços em branco extras do início e do final
nome = input("Qual o seu nome? ").strip()

# Divide o nome em partes separadas usando espaços como delimitador e armazena em uma lista
separado = nome.split()

# Exibe o primeiro nome do usuário, que é o primeiro elemento da lista 'separado'
print('Seu primeiro nome é {}'.format(separado[0]))

# Exibe o último nome do usuário, que é o último elemento da lista 'separado'
print('Seu último nome é {}'.format(separado[-1]))
