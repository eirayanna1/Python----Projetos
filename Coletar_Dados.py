# Título sugerido: Análise de Idades e Gêneros

soma = 0  # Inicializa a variável para armazenar a soma das idades

# Loop para coletar informações de 4 pessoas
for c in range(4):
    n1 = str(input("Qual o seu nome?")).strip()  # Solicita o nome da pessoa
    n2 = int(input("Qual a sua idade?"))  # Solicita a idade da pessoa
    n3 = str(input("Qual o seu sexo?")).strip().upper()  # Solicita o sexo da pessoa e converte para maiúsculas

    soma += n2  # Adiciona a idade da pessoa à soma total

# Calcula a média das idades
média = soma / 4
print("A média total de idade é de {}".format(média))

# Verifica se há mulheres com menos de 20 anos e conta quantas são
if n3 == "FEMININO" and n2 < 20:
    soma += n3  # Incrementa o contador de mulheres com menos de 20 anos
    print('A quantidade de mulheres com menos de 20 anos é de {}.'.format(soma))
