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
pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
}

pessoa2 = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'sobrenome': 'Kumamoto1',
    'sobrenome': 'Kumamoto2',
    'sobrenome': 'Kumamoto3',
}
# uso do len em dicionário é para contagem das chaves
p(len(pessoa))
p('---')

# note que chaves repetidas só será utilizada a última chave
p(len(pessoa2))
p('---')

# quando usa-se keys retorna um dicionário de chaves
p(pessoa.keys())
p('---')
p(pessoa2.keys())
p('---')

# lembre-se que os dados podem ser convertidos
p(tuple(pessoa.keys()))
p(list(pessoa.keys()))
p('---')

# verificando os valores das chaves que também retorna um dicionário. também pode realizar a coerção
p(pessoa.values())
p('---')

# aplicando num laço for
for valor in pessoa.values():
    p(valor)
p('---')

# usando items retorna um dicionário com os itens (que são tuplas)
p(pessoa.items())
p('---')

# parte interessante disso é usar dentro de um laço for para retornar duas variáveis
for chave, valor in pessoa.items():
    p(chave, valor)
p('---')

# o setdefault server em caso de um dicionário não ter uma chave e ele atribuir uma chave:valor padrão
pessoa.setdefault('idade', None) # neste caso o None faz com que evite um erro dentro do python e 
                                 # não obrigatório ser None, por der qualquer número. mas se o dicionário 
                                 # tiver um campo idade, o setdefault é iginorado
p(pessoa['idade'])
p('---')

#exemplo
pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'idade': 41,
}
pessoa.setdefault('idade', None)
p(pessoa['idade'])
p('---')