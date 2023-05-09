'''
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
'''
# a forma mais usada para dicionários
pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
}

p(pessoa, type(pessoa))
p('---')
# outra forma mas menos usual
pessoa = dict(nome='Eiji', sobrenome='Kumamoto')

p(pessoa, type(pessoa))
p('---')

# um dicionário com mais informações
pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'idade': 41,
    'altura': 1.84,
    'endereços': [ # aqui temos uma lista (com um dicionário de endereços) dentro do dicionário
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
p(pessoa, type(pessoa))
p('---')

# acessando um índice com uma string
p(pessoa['nome'])
p(pessoa['sobrenome'])
p('---')

# também usando um laço for
for chave in pessoa:
    p(f'{chave}: {pessoa[chave]}')

p('---')

