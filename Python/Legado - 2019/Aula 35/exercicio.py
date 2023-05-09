'''Faça um programa que some os valores de todos os produtos (independente da quantidade) usando list comprehension'''

carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

total = sum([float(y) for x,y in carrinho])
print (total)