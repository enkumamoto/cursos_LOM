'''
O python permite que as variáveis troquem de valores entre elas.
'''
x = 10
y = 'Eiji'
z = 'Kumamoto'

# Em outras linguagens a coisa seria desta forma:
# z = x
# x = y
# y = z

# Já em python basta fazer assim:
x, y, z = y, x, z

print (f'x={x} e y={y} e z={z}')
'''
Obs: Não há limites para quantidade de variáveis.
'''
