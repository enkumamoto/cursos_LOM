# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
p(list(range(10)))
p('---')

# como normalmente fazem
lista = []
for numero in range(10):
    lista.append(numero)
p(lista)
p('---')

# com list comprehension
lista = [numero for numero in range(10)]
p(lista)
p('---')

# fazendo multiplicação
#a = int(input('Digite um multiplicador: '))
a = 2
lista = [
    numero * a
    for numero in range(10)
]
p(lista)
p('---')

# mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10},
    {'nome': 'p3', 'preço': 30},
    
]
novos_produtos = [ # criando lista a partir da lista de dicionários
    produto
    for produto in produtos # este for pega uma linha por iteração
]
p(novos_produtos)
p('---')

# também podemos desempacotar a lista e usar um separador 
p(novos_produtos)
#print(*novos_produtos, sep='\n')
p('---')

# otmizando o for
produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10},
    {'nome': 'p3', 'preço': 30},
    
]
novos_produtos = [
    produto ['nome']
    for produto in produtos
]
p(novos_produtos)
p('---')

# pode-se criar novos dicionários
novos_produtos = [
    {'nome': produto['nome'], 'preço': produto['preço']}
    for produto in produtos
]

p(novos_produtos)
p('---')

# ou desta forma
novos_produtos = [
    {**produto}
    for produto in produtos
]

p(novos_produtos)
p('---')

# se quiser da para manipular os valor dos produtos dentro do laço, por exemplo aumentar em 5%
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05} # aumentando em 5%
    for produto in produtos
]

p(novos_produtos)
p('---')

# aumentando em 5% o valor dos produtos com preço maior que 20
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05} if produto['preço'] > 20 else {**produto} for produto in produtos
]

p(novos_produtos)
p('---')

# laço for em list comprehension
lista = [n for n in range(10)]
print(lista)
print("---")

# inclusindo números menores que 5
lista = [n for n in range(10) if n < 5] # o if age como filtro do for enquanto a condição for verdadeira
print(lista)
print("---")

# deixando claro, o que está a esquerda do for é mapeamento e a direita é filtro
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05} 
    if produto['preço'] > 20 else {**produto} 
    for produto in produtos
    if produto['preço'] > 10 #aqui não incluirá o 10
]
p(novos_produtos)
print("---")

# o valor so preço calculado é o da lista acima, caso queria calcular 
# em cima de valor novo deve-se fazer da forma abaixo para incluir 
# somente o produto com valor mais alto, no caso o de 31.5
novos_produtos = [
    {**produto, 'preço': produto['preço'] *1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] *1.05) > 10
]
p(novos_produtos)
print("---")