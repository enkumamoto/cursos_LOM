'''
Agrupamento de elementos em um dicionário
'''
# importaremos a função groupby do itertools
from itertools import groupby

# para melhor entender cria-se uma lista com dicionário dentro dela
alunos = [
    {'nome': 'Eiji', 'nota': 'A'},
    {'nome': 'Ananda', 'nota': 'B'},
    {'nome': 'Duda', 'nota': 'A'},
    {'nome': 'Nina', 'nota': 'C'},
    {'nome': 'Junior', 'nota': 'D'},
    {'nome': 'José', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Zezinho', 'nota': 'A'},
    {'nome': 'Chico', 'nota': 'C'},
    {'nome': 'Vanessa', 'nota': 'B'},
]

'''
o groupby necessita que os dados estejam em ordem para funcionar devidamente, mas para facilitar
será usado a função lambda junto com um sort.
'''
# alunos.sort(key=lambda item: item['nota'])

# o for ajuda a visualiza melhor a saída dos dados
# for aluno in alunos:
#     print (aluno)

'''
para deixar o código sem muita repetição, pois usariamos 'lambda item: item['nota']' novamente
para que o código retornasse as informações de forma devida, faremos o código da forma abaixo:
'''
ordena = lambda item: item['nota']  # passamos a expressão como valor de variável
alunos.sort(key=ordena)  # usamos a variável como chave para a organização por notas
alunos_agrupados = groupby(alunos,ordena)  # agrupando os dados

for agrupado in alunos_agrupados:
    print(agrupado)
print('---')
'''
a saída do laço for apresentará um resutado que na nota A tem um grupo de alunos,
nota B tem outro grupo e assim por diante, mas não apresenta os nomes dos alunos.
para resolver esse problema deve-se modificar o laço for como abaixo:'''
ordena = lambda item: item['nota']
alunos.sort(key=ordena)  # 1
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')  # agrupamento é o grupo de quem tem a nota
    for aluno in valores_agrupados:
        print(aluno)  # será exibido os alunos com a nota
        # print(len(aluno))  # aqui apresenta a quantidade de valores por dicionário
    print()
print('---')

'''1 - perceba que se retirar a ordenação dos dados o laço for apresentará os dados de forma estranha, como se cada
       passagem fosse um novo dado inserido.'''

# Para o código ficar mais organizado e limpo pode-se escrever da forma abaixo.
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))  # transformando a contagem em lista. len é um iterador laços for após esta linha não funcionará porque o iterador já esgotou os dados. então o for deve vir antes.
    print(f'{quantidade} alunos que tiraram a nota {agrupamento}')
print('---')

''' atenção se a lista receber os dados de forma repetida, no caso mesmo nome de aluno e a mesma nota, o programa contabilizará
    normalmente e somará todos os dados sem reconhecer a repetição..'''

# colocando um laço for para exibir o nome de alunos e não contabilizando quantos alunos de acordo com a nota tirada
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    for aluno in valores_agrupados:  # percebe-se que o len na próxima linha não funciona como no código acima.
        print (aluno)

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos que tiraram a nota {agrupamento}')
print('---')

# solucionando o caso acima
from itertools import tee  #primmeiro importar o módulo tee

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos,ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # usou-se duas variáveis recebendo o mesmo valor e aplicando em lugares diferentes
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:  # trocou-se a variável valores_agrupardo por va1
        print (f'\t{aluno}')  # o \t é um tab

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos que tiraram a nota {agrupamento}')
    print()
print('---')

'''
O que aconteceu acima foi, o uso do módulo tee para gerar cópias de um iterador (no caso va1 e va2). 
como se sabe iteradores são finitos e assim que esgotados um novo laço não terá dados para trabalhar.
com isso o usso do tee resolve o problema para usar no for e no len.
'''