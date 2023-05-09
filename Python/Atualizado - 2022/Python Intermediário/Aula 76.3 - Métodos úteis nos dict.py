'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
# deve-se ter muita atenção ao trabalhar com dicionários
# pois os dados são mutáveis. veja o exemplo abaixo
d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1 # aqui tem a intenção de fazer uma "cópia" do d1

d2['c1'] = 1000 # informando a mudança de c1 em d2

p(d1)
p('---')

'''
como pode ver, c1 teve o valor mudado por que d1 e 
d2 por serem o mesmo dicionário na memória.
neste caso deve-se usar o método copy
'''
d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1.copy() # aqui fez-se uma "cópia rasa" do d1

d2['c1'] = 1000 # informando a mudança de c1 em d2

p(f'dicionário d1: {d1}')
p(f'dicionário d2: {d2}')
p('---')

# adicionando uma lista ao dicionário
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2] 
}

d2 = d1.copy() # aqui fez-se uma "cópia rasa" do d1

d2['c1'] = 1000
d2['l1'][1] = 9999 # alterando o dado da lista

p(f'dicionário d1: {d1}')
p(f'dicionário d2: {d2}')
p('---')

'''
Como pode ver a lista em d1 e d2 receberam a mesma 
alteração, isso por que o método copy faz cópia rasa
e alterou as duas listas (que também apontam para o 
mesmo id de memória)
o .copy() por padrão faz cópia rasa, para fazer uma 
cópia sem afetar uma a outra com as alterações, deve-se
importar o copy
'''
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2] 
}

d2 = copy.deepcopy(d1) # aqui fez-se uma "cópia total" do d1 (cópia em todos os níveis)

d2['c1'] = 1000
d2['l1'][1] = 9999 # alterando o dado da lista

p(f'dicionário d1: {d1}')
p(f'dicionário d2: {d2}')
p('---')