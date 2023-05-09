'''
Exercício
Exiba os índices da lista
'''

lista = ['Maria', 'Helena', 'Luiz']
indice = 0

for nome in lista:
    print(f'{nome} está no índice {indice}')
    indice += 1
print('---')

'''resposta do professor'''
lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(f'{lista[indice]} está no índice {indice}')
print('---')