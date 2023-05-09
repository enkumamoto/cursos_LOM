'''
Dicionários são similares as listas, o que muda é que no dicionário o user controla o índice.
'''
d1 = {'chave1': 'valor da chave'}  # exemplo de dicionário
d1['nova_chave'] = 'valor da nova chave'  # acrescentando nova chave ao dicionário

print(d1['chave1'])  # acessando uma das chaves.
print(d1)  # mostra o dicionário completo
print('---')

# existe outra forma de construir dicionários
d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')

print(d2['chave1'])  # acessando uma das chaves.
print(d2)  # mostra o dicionário completo
print('---')

# Lembre-se que as chaves do dicionário são únicas, ou seja, se valores diferente
# recebem a mesma chave, o python retorna o último valor
d3 = {'chave1': 'valor da chave', 'chave1': 'valor da chave', 'chave1': 'Ananda'}
print(d3['chave1'])
print(d3)  # mostra 'chave1':'Ananda' como dicionário completo
print('---')

# mas se os valores são iguais, mas com chaves diferentes
d4 = {1: 'valor da chave', 2: 'valor da chave', 3: 'Ananda', 4: 'valor da chave', 5: 'valor da chave'}
print(d4[3])
print(d4)
print('---')

# geralmente as chaves do dicionário são str, mas também pode ser número int ou tupla
d5 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}
print(d5[(1, 2, 3, 4)])  # acessando item com a tupla
print('---')

# uma coisa que pode vir a acontecer é tentar acessar uma chave que não existe.
# acessando com uma chave que não existe sem checagem retornará erro. mas como há uma inclusão da chave e um if realizando
# checagem, o print com oi funcionará.
d5 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}

d5['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d5:
    print(d5['naoexiste'])
print("Oi!")
print('---')

# abaixo há a captura da nova chave e confirmação com uma checagem
d6 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}
d6['nomedachave'] = 'Agora ela existe'

if d6.get('nomedachave') is not None:  # usando o '.get' para pegar nova chave
    print(d6.get('nomedachave'))
print('Oi!')
print('---')

# Também existem formas para atualizar valores de chaves
d7 = {
    'str': 'valor',  # temos aqui a chave 'str
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}
# d7 ['str'] = 'Agora ela existe'  # trocamos 'nomedachave' por 'str'

if d7.get('str') is not None:
    print(d7.get('str'))  # no output percebera que nada muda, mas para o python a chave 'str' tem o valor 'Agora ela existe".
                          # Agora Testa comentando a linha 73...
print('Oi!')  # Perceba que agora o output muda para 'valor' que é o valor de 'str'
print('---')

# outra forma de atualização de chave
d8 = {
    'str': 'valor',
    123: 'Outro Valor',
    (1, 2, 3, 4): 'Tupla',
}

d8.update({'nova_chave': 'supimpa'})

if d8.get('nova_chave') is not None:
    print(d8.get('nova_chave'))
print('Oi!')
print('---')

# caso queira deletar algum item do dicionário deve usar a palavra reservada del
d9 = {
    'string': 'valor',
    123: 'Outro Valor',
    (1, 2, 3, 4): 'Tupla',
}

del d9['string']  # aqui deletou-se a chave str
print(d9)
print('---')

# outra forma de checagem de chaves de um dicionário
d10 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print('str' in d10)
print('valor' in d10.values())  # aqui realiza checagem do valor e da output do valor booleano
print('str' in d10.keys())  # aqui realiza checagem do chave e da output do valor booleano
print(len(d10))  # exibe a quantidade de pares chave:valor dentro do dicionário.
print('---')

# também pode iterar sobre os dicionários
d11 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'Tupla',
}

print('Chaves do dicionário')
for k in d11:  # exibirá as chaves
    print(k)

print ('\nValores das chaves')
for v in d11.values():  # exibirá os valores
    print(v)

print ('\nVisualizando chaves e valores')
for i in d11.items():  # exibirá chaves e valores
    print(i)
# ou
print('\n')
for k ,v in d11.items():
    print(k,v)

# da forma acima pode-se acessar por meio de índices.
print('---')

# Iterando dicionários com dicionários
clientes = {
    'cliente1' : {
        'nome' : 'Eiji',
        'sobrenome' : 'Kumamoto',
    },
    'cliente2' : {
        'nome' : 'Ananda',
        'sobrenome' : 'Seabra',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Eduarda',
    },
}
print('Chaves do dicionário')
for k in clientes:  # exibirá as chaves
    print(k)

print ('\nValores das chaves')
for v in clientes.values():  # exibirá os valores
    print(v)

print ('\nVisualizando chaves e valores')
for i in clientes.items():  # exibirá chaves e valores
    print(i)
# ou
print('ou')
for k ,v in clientes.items():
    print(k,v)
print('\n')
# também loop for com outro for:
for clientes_k, clientes_v in clientes.items():  # o primeiro for é responsável pelo loop completo
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')  # /t gera identação
print('---')

'''
Cuidado a forma abaixo não cria novo objeto e sim iguala as variáveis.
Aprofundando mais, os dois objetos apontam para o mesmo local da memória.
'''
d12 = {1 : 'a', 2 : 'b', 3 : 'c'}
v = d12

print (d12)
print(v)
print('\n')

v[1] = 'Eiji' # mudando o valor da chave 1
print (d12)
print(v)
print('---')

'''
O python permite uma shalow copy(cópia rasa) do dicionário da seguinte forma
'''
d13 = {1 : 'a', 2 : 'b', 3 : 'c'}
v = d13.copy()  # o '.copy()' usa o dicionário como referência e não faz uma cópia. Abaixo um exemplo de um comportamente usando o '.copy'

print (d13)
print(v)
print('\n')

v[1] = 'Eiji' # mudando o valor da chave 1
print (d13)
print(v)
print('---')

d13 = {1 : 'a', 2 : 'b', 3 : 'c', 'd' : ['Eiji', 'Kumamoto']}  # Criado mais um índici no dicionário e colocando lista como valor.
v = d13.copy()

print (d13)
print(v)
print('\n')

v[1] = 'Eiji'  # mudando o valor da chave 1
v['d'] [0] = 'Joãozinho'  # mudando o nome eiji para joãozinho
print (d13)
print(v)
'''
Percebe-se que no output nos dois dicionários o nome eiji é mudado para joãozinho.
Isso acontece porque listas são mutáveis.
Não funciona para alterar intens da tuplas, mas pode mudar o valor da chave (trocar a tupla inteira)
'''
print('---')

# Para realizar uma cópia real do dicionaŕio
import copy  # módulo copy
d14 = {1 : 'a', 2 : 'b', 3 : 'c', 'd' : ['Eiji', 'Kumamoto']}  # Criado mais um índici no dicionário e colocando lista como valor.
v = copy.deepcopy(d14) # usando o copy.deepcopy(), ele fará uma cópia do dicionário mas deixando os dois independentes.

print (d14)
print(v)
print('\n')

v[1] = 'Eiji'  # mudando o valor da chave 1
v['d'] [0] = 'Joãozinho'  # mudando o nome eiji para joãozinho
print (d14)
print(v)
print('---')

# transformando lista ou tupla em dicionário
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
    ('a1', 1),
    ('a2', 2),
    ('a3', 3),
]
d15 = dict(lista)
print(d15)
print('---')

d16 = {
    1:2,
    2:3,
    3:4,
    4:5,
}
print(d16)
print('\n')
# Se quiser eliminar a última chave do dicionário
d16.pop(4)
print(d16)
print('\n')
# Para eliminar o último item seja ele qual for
d16 = {
    1:2,
    2:3,
    3:4,
    4:5,
}
d16.popitem()
print(d16)
print('---')

# Concatenando dicionário
d16 = {
    1:2,
    2:3,
    3:4,
    4:5,
}
d16.update(d15)
print(d16)