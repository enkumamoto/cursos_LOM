# Dictionary Comprehesion e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())
print('---')

#checando chave e valor com o for
for chave, valor in produto.items():
    print(chave, valor)
print('---')

# vamos criar um novo dicionário comprehension
dc = {
    chave: valor
    for chave, valor
    in produto.items()
}
print(dc)
print('---')

# realizando checagem de tipo (melhor forma)
dc = {
    chave: valor.upper() # sabe-se que upper é para string. então caso não tenha produto em estoque o programa retorna um ESGOTADO
    if isinstance(valor, str) else valor # checa se há str se não retorna o valor numérico
    for chave, valor
    in produto.items()
}
print(dc)
print('---')

# a forma abaixo da certo mas abre margem para erro
dc = {
    chave: valor # aqui sabe-se que passará um valor em float
    if isinstance(valor, (int, float)) else valor.upper() # checa se o valor é valor é int ou float, se não for o valor deve sair em maiúsculo
    for chave, valor
    in produto.items()
}
print(dc)
print('---')

# caso não queira incluir chaves
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria' #desta forma só incluirá categoria
}
print(dc)
print('---')

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria' #desta forma não incluirá categoria
}
print(dc)
print('---')

# criando dict a partir de uma lista de tuplas
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
    ('d', 'valor d'),
    ('e', 'valor e'),
    ('f', 'valor f'),
    ('g', 'valor g'),
    ('h', 'valor h'),    
]

dc = {
    chave: valor 
    for chave, valor in lista
}
print(dc)
print(dict(lista)) # usando a função dict
print('---')

# apresentando set comprehension
s1 = {i for i in range(10)}
print(s1)
print('---')

#ou
print(set(range(10)))
print('---')

# a lógica pode ser de acordo com a finalidade do usuário
s1 = {i ** 2 for i in range(10)} # elevando todas as passagens do for ao quadrado
print(s1)
print('---')

# ou
s1 = {2 ** i for i in range(10)} # elevando dois a todas as passagens do i no for
print(s1)
print('---')