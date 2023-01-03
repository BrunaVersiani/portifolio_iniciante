#Criando Produtos e preços
product1_nome, product1_preco = 'laranja', 10.95
product2_nome, product2_preco = 'Tomate', 5.30
product3_nome, product3_preco = 'Maça', 8.75
product4_nome, product4_preco = 'Melão', 10.99
product5_nome, product5_preco = 'pera', 15.95
product6_nome, product6_preco = 'uva', 7.98
product7_nome, product7_preco = 'cebola', 3.15
product8_nome, product8_preco = 'pimenta', 9.99
product9_nome, product9_preco = 'coco', 5.00
product10_nome, product10_preco = 'alface', 1.99


# Informações do estabelecimento
empresa_nome = 'Sacolão Oliveira'
empresa_endereco = 'Av. Geraldo, 1275, Bairro: Cristiano'
empresa_cidade = 'Belo Horizonte / MG'


# Menssagem
menssagem = 'Obrigada pela preferencia! Volte sempre. '


# decoração
def decoracao():
    print('*' * 50)


# print informações da empresa
print(f'\t\t{empresa_nome.title()}')
print(f'\t\t{empresa_endereco.title()}')
print(f'\t\t{empresa_cidade.title()}')


# decoração
decoracao()


# Print produto e preço
print('\t\tProduto \tPreço')


# produtos comprados
print(f'\t\t{product1_nome.title()}\t\tR${product1_preco}')
print(f'\t\t{product5_nome.title()}\t\tR${product5_preco}')
print(f'\t\t{product8_nome.title()}\t\tR${product8_preco}')
print(f'\t\t{product10_nome.title()}\t\tR${product10_preco}')
print(f'\t\t{product4_nome.title()}\t\tR${product4_preco}')
print(f'\t\t{product3_nome.title()}\t\tR${product3_preco}')
print(f'\t\t{product7_nome.title()}\t\tR${product7_preco}')


# decoração
print('=' * 50)


# Calculo total da compra
total = (product1_preco + product5_preco + product8_preco + product10_preco + product4_preco + product3_preco + product7_preco)
print(f'\t\t{"Total"}\t\tR${total}')


# print mensagem
print(f'\n\t{menssagem}\n')


# decoração
decoracao()
