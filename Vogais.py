# Definindo a tupla de palavras
palavras = ('amor', 'escola', 'janela')

# Lista de vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Iterando sobre cada palavra na tupla
for palavra in palavras:
    vogais_na_palavra = []  # Lista para armazenar as vogais encontradas em cada palavra
    # Iterando sobre cada letra na palavra
    for letra in palavra:
        if letra in vogais:  # Verifica se a letra é uma vogal
            vogais_na_palavra.append(letra)  # Adiciona a vogal encontrada na lista
    # Imprime as vogais encontradas na palavra, separadas por vírgula
    print(f"Vogais em '{palavra}': {', '.join(vogais_na_palavra)}")
