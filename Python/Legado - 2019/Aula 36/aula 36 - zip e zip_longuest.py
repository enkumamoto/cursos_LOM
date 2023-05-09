"""
Ambas são nativas no python
Zip - Unindo iteráveis
Zip_longuest - Itertools
"""

# Vamos supor que temos uma lista de cidades entre partes do código

## Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'João Pessoa', 'Natal']

## Código
estados = ['SP', 'MG', 'BA', 'PB']

# A ideia é unir as duas listas onde a cidade esteja associada ao estado

cidades_estados = zip(cidades, estados)  # usando o zip, unificará as duas listas

for i in cidades_estados:  # com o for ele passará dentro das listas até esgota-las
    print (i)
print('---')
# Como pode ver, a variável acima cria tuplas com a cidade como chave, mas invertendo a posição o estado passa ser a chave
cidades_estados = zip(estados, cidades)
print (cidades_estados)  # o print retornará <zip object at 0x7fbc0f01e800> que aponta para um ponto da memória
print('---')

# caso queira que o output da variável seja uma lista podemos dar o print da forma abaixo
print (list(cidades_estados))
print('---')

# ou como dicionário
cidades_estados = zip(estados, cidades)
print (dict(cidades_estados))
print('---')

# Obs.: o zip unifica tendo como referência a menor lista.

# Agora para usar o zip_longest teremos que importar o módulo e usaremos as variáveis acima e trocar o zip por zip_longest.
from itertools import zip_longest, count

cidades_estados = zip_longest(cidades, estados)

for i in cidades_estados:
    print (i)
print('---')

cidades_estados = zip_longest(estados, cidades)
print (cidades_estados)
print('---')

print (list(cidades_estados))
print('---')

cidades_estados = zip_longest(estados, cidades)
print (dict(cidades_estados))
print('---')

""" Perceba que tudo foi unificado a partir da maior lista e que o item que não consegue ser associado com a lista menor recebe um 'none'
Caso queira que o valor none seja substituido por qualquer outra coisa, deve-se usar fillvalue='o_que_deseja'"""
cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')

for i in cidades_estados:
    print (i)
print('---')

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
print (cidades_estados)
print('---')

print (list(cidades_estados))
print('---')

cidades_estados = zip_longest(estados, cidades, fillvalue='Estado')
print (dict(cidades_estados))
print('---')

# Supondo que usaremos um gerador de índicies para aparecer dentro da nossa lista e demais.
# Recomenda-se não usar zip_longest pois gerará um looping infinito, então use o zip
from itertools import count  # importando o módulo count

indice = count()  #gerador de índice ou contador
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'João Pessoa', 'Natal']
estados = ['SP', 'MG', 'BA', 'PB']

cidades_estados = zip(
    indice,
    cidades,
    estados,
)

for i in cidades_estados:
    print (i)
print('---')

indice = count()  #gerador de índice ou contador
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'João Pessoa', 'Natal']
estados = ['SP', 'MG', 'BA', 'PB']

cidades_estados = zip(
    indice,
    estados,
    cidades,
)

print (cidades_estados)
print('---')

indice = count()  #gerador de índice ou contador
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'João Pessoa', 'Natal']
estados = ['SP', 'MG', 'BA', 'PB']

print (list(cidades_estados))
print('---')

# ou de forma desempacotada
for indice, estados, cidades in cidades_estados:
    print(cidades_estados)
print('---')
