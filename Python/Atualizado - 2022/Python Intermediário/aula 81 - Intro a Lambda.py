'''
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única
expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
'''
lista = [23,5,763,7,3,64,2345,37,4,32,23]
lista.sort()
p(lista)
p('---')

# invertendo a ordem dos números
lista.sort(reverse=True)
p(lista)
p('---')

'''
o python precisa ser ensinado a ordenar algumas coisas, no caso a lista abaixo.
o sort() faz comparativo com maior e menor para ordenar números.
'''
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
    {'nome': 'Ananda', 'sobrenome': 'Seabra'},
    {'nome': 'Eiji', 'sobrenome': 'Kumamoto'},
    {'nome': 'José', 'sobrenome': 'alves'},
    
]

ordem = int(input("Quer ordenar por [1]Nomes ou [2]Sobrenomes: "))

if ordem == 1:
    # ordenando por nome
    def ordena(item):
        return item ['nome']

    lista.sort(key=ordena) # a key é uma função que tem ter uma definição de função

    for item in lista:
        p(item)
    p('---')

elif ordem == 2:
    # ordenando por sobrenome
    def ordena(item):
        return item ['sobrenome']

    lista.sort(key=ordena) # a key é uma função que tem ter uma definição de função

    for item in lista:
        p(item)
    p('---')

else:
    p('Opção inválida')

'''
python usa tabela alfanumérica unicode, ou seja, 
ele difere maiúscula de minúscula, por isso que 
o José alves aparece por último
'''

# usando lambda
ordem = int(input("Quer ordenar por [1]Nomes ou [2]Sobrenomes: "))

if ordem == 1:
    # ordenando por nome
    lista.sort(key=lambda item: item['nome']) # o lambda elimina o uso de função
    for item in lista:
        p(item)
    p('---')

elif ordem == 2:
    # ordenando por sobrenome
    lista.sort(key=lambda item: item['sobrenome'])

    for item in lista:
        p(item)
    p('---')

else:
    p('Opção inválida')

# uma outra forma
def exibir(lista):
    for item in lista:
        p(item)
    p('---')
    p()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)