# Criando uma lista de produtos com seus preços em uma única tupla
produtos_precos = (
    ("Produto 1", 10.99),
    ("Produto 2", 20.49),
    ("Produto 3", 15.75),
    ("Produto 4", 30.25),
    ("Produto 5", 8.50)
)

# Imprimindo a tabela formatada
print("Lista de Produtos e Preços:")  # Imprime o título da tabela
print("{:.<15} {:.>10}".format("Produto", "Preço"))  # Imprime o cabeçalho da tabela
print("-" * 25)  # Imprime uma linha separadora

# Itera sobre a lista de produtos e preços e os imprime formatados na tabela
for produto, preco in produtos_precos:
    print("{:<15} R${:<10.2f}".format(produto, preco))  # Imprime cada linha da tabela com o nome do produto e o preço
