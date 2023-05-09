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

# usando método get
p1 = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'idade': 41,
}
p(p1.get('nome'))
p('---')

# usando o pop
nome = p1.pop('nome')
p(nome)
p(p1)
p('---')

# usando o popitem
p1 = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'idade': 41,
}
ultima_chave = p1.popitem()
p(p1)
p('---')

# usando update, que tbm aceita argumento nomeados
p1.update({
    'idade': 41,
    'endereço': None,
})
p(p1)
p('---')

# update com tuplas
tupla = ('CEP', None),
p1.update(tupla) # tbm funciona com listas
p(p1)
p('---')