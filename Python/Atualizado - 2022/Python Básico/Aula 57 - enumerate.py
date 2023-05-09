'''
enumerate - enumera iteráveis (índices)
'''
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

lista_enumerada = enumerate(lista)

print(lista_enumerada) # exibirá um ID de memória
print(next(lista_enumerada)) # exibirá o primeiro item em forma de tupla
print('---')

'''
podemos usar o laço for com este recurso
'''
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

lista_enumerada = enumerate(lista)

print(lista_enumerada)
for item in lista_enumerada:
    print(item)
print('---')

"""
um problema que é gerado acima é que da forma que está o for
consome todos os valores do iterador, ou seja, se tentar usar
outro for não haverá valores para exibir.
para resolver esse problema deve-se colocar o enumerate dentro 
do for
"""
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

for item in enumerate(lista): # desta forma, pode-se usar vários laços for
    print(item)

for item in enumerate(lista):
    print(item)

for item in enumerate(lista): # desta forma, pode-se usar vários laços for
    print(item)
print('---')

"""
mas caso não queira usar o for anterior e colocar o enumerate como valor de variável,
então pode-se converter este valor em lista
"""
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada) # neste caso, será criada uma lista com tuplas
# for item in lista_enumerada: # descomentando está parte, verá a sequência
#     print(item)
print('---')

'''
também pode-se alterar o ponto de início da contagem do enumerate
'''
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

lista_enumerada = list(enumerate(lista, start=19))
print(lista_enumerada)
print('---')

"""
separando os índices
"""
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

lista_enumerada = list(enumerate(lista))

for item in lista_enumerada:
    indice, nome = item # aqui a primeira variável recebe o valor do enumerate (índice) e a segunda variável o valor que foi enumerado (nome)
    print(indice, nome) 
print('---')

'''
ou
'''
lista = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
lista.append('Malu')

for indice, nome in enumerate(lista):
    print(indice, nome) 
print('---')

'''
e também dessa forma
'''
for tupla_enumerada in enumerate(lista): # neste for separa-se o índice do valor em linhas distintas 
    print("FOR da Tupla:")
    for valor in tupla_enumerada:
        print(f'\t{valor}')
print('---')