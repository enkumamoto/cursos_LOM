"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""
nome = 'Eiji'
preco = 1000.1327462789345
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' %(1500, 1500))