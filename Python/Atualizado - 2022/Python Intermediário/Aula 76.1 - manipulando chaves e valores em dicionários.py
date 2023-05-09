# Manipulando chaves e valores em dicionários
pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
    'idade': 41,
    'altura': 1.84,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
p(pessoa['nome'])
p('---')
#formas de criar índices no dicionário
pessoa = {}
pessoa['nome'] = "Duda"

#acessando a chave
p(pessoa['nome'])
p('---')

# usando chaves dinâmicas
chave = 'nome'
pessoa[chave] = "Nande"
p (pessoa[chave])
p('---')

# apagando chave
chave = 'nome'
pessoa[chave] = "Ananda"
pessoa['sobrenome'] = "Seabra"
p (pessoa)
p('---')

#deletando chave
chave = 'nome'
pessoa[chave] = "Ananda"
pessoa['sobrenome'] = "Seabra"
del pessoa['sobrenome']
p (pessoa)
p('---')

'''
deve-se ter atenção com a exclusão de chaves, pois isso 
pode atrapalhar o programa ao tentar acessar uma chave
que não existe.
'''