"""
Compreensão de dicionários segue a mesma linha de raciocínio das listas com diferenças sutís
"""
# Exemplo
list1 = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

# Usando compreensão de dicionário
d1 = {x: y for x, y in list1}  # Tradução: Criando Dicionário para Chave e Valor (x e y) que estão na list1

# Da mesma forma que poderia ser usado a linha abaixo
#d1 = dict(list1)
print (d1)

# Pode realizar operações matemáticas, mas deve-se ficar atento a mutiplicar strings, elas serão duplicadas, mas
# se o valor da chave for um número, a multiplicação será normal.
list2 = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d2 = {x: y*2 for x, y in list2}
print (d2)

# Também pode-se usar o upper
list3 = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d3 = {x: y.upper() for x, y in list3}  # Neste caso só o y (valor) ficará em maiúsculo, mas pode usar no x (chave) também.
print (d3)

# Usando o ennumerate(range())
d4 = {x: y*2 for x, y in enumerate(range(5))}
print (d4)

# Usando somente o range()
d5 = {x for x in range(5)}
print (d5, type(d5))  # Será apresentado que d5 é um set (conjunto)

# Gerando chave com range
d6 = {f'chave_{x}': x**2 for x in range(5)}
print(d6)
