'''
Combinations, Permutation e Product - Itertools

Combinações - Não importa a ordem e os valores únicos não se repetem
Permutações - Ordem importa e os valores únicos não se repetem

Produto - Ordem importa e repete valores únicos
'''

# importando o combinations pode-se combinar os elementos de uma lista por exemplo. lembre-se que o combinations que uma combinação A com B
# é a mesma coisa que B com A e nunca A com A
from itertools import combinations, permutations, product

pessoas = ['Eiji', 'Andanda', 'Carlos', 'Julia', 'Luiz', 'Rafael']
for grupos in combinations(pessoas, 3):
    print (grupos)
print('---')

# usando o permutations percebe-se que a coisa muda um pouco. o resultado de A com B e B com A é érmitida, mas não o A com A
pessoas = ['Eiji', 'Andanda', 'Carlos', 'Julia', 'Luiz', 'Rafael']
for grupos in permutations(pessoas, 3):
    print (grupos)
print('---')

# para ter todas as combinações possíveis deve-se importar o product
pessoas = ['Eiji', 'Andanda', 'Carlos', 'Julia', 'Luiz', 'Rafael']
for grupos in product(pessoas, repeat=2):
    print (grupos)
print('---')