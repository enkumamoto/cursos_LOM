'''
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

# A lista pode recebe qualqeur tipo de valor
text = 'Valor'
#        0    1    2    3   4
list = ['A', 'B', 'C', 'D','E']  # O acesso a lista é por meio de índice.
#     -  5    4    3    2   1

string = 'ABCDE'

print (string[1])
print (list[1])
print ('---')

# exemplo
text = 'Valor'

list = ['A', 'Bacana', 'C', 'D','E']  # Subustituindo o B por bacana, será apresentado Bacana no print abaixo.

string = 'ABacanaCDE'

print (string[1])  # Aqui será apresentado o B e não bacana, pois o índice 1 é o B e não igual como na lista.
print (list[1])
print (list[0:4])  # Aqui delimita-se de onde até onde será apresentado na tela
print (list[-1])  # Aqui apresenta o último item da lista. (vide aula 17)
print ('---')

# Pode-se manipular a lista usando append, insert, pop, del, clear, extend, +;

l1 = [1,2,3]
l2 = [4,5,6]
print (l1)
print (l2)
print ('---')

# Caso queira concatenar as duas listas
l3 = l1 + l2
print (l1)
print (l2)
print (l3)
print ('---')

# pode-se estender a lista usando o .extend
l4 = [1,2,3]
l5 = [4,5,6]
l4.extend('a')
print (l4)
print (l5)
print ('---')

# para incluir um valor ao último índice da lista, usa-se o .append
l6 = [1,2,3]
l7 = [4,5,6]
l7.append('b')
print (l6)
print (l7)
print (l7[3])
print ('---')

# já o .insert coloca valor no índice desejado da lista
l8 = [1,2,3]
l9 = [4,5,6]
l9.insert(0, 'banana')  # inseriu banana no índice 0 (primeira posição da lista)
print (l8)
print (l9)
print (l9[0])
print ('---')

# com o .pop pode-se eliminar o valor do último índice.
l10 = [4,5,6]
print (l10)
l10.insert(0, 'banana')
print (l10)
l10.pop()
print(l10)
print ('---')

# mas para usar o del deve ter atenção. caso queira deletar um único valor do índice 4
l11 = [1,2,3,4,5,6,7,8,9]

del (l11 [4])  # deletará o úmero 5

print (l11)
print ('---')

# pode deletar em range, mas lembre-se que no range o último índice mencionado não será deletado.
l12 = [1,2,3,4,5,6,7,8,9]

del (l12 [3:5])  # deletará os números 4 e 5
print (l12)
l12.insert(0,'banana')
print(l2)
del(l2[0])
print(l2)
print ('---')

# Uso de max e min dentro de listas
l13 = [1,2,3,4,5,6,7,8,9]
print(max(l13))  # mostrar o maior número da lista
print(min(l13))
print ('---')

'''
Python tem uma função built-in chamada list que serve para criação de listas.
Esta função usa objetos iteráveis, como por exemplo o range.
'''
l14 = list(range(1,10))
print (l14)

# também podemos interagir com o laço for
soma = 0
for valor in l14:
    soma = soma + valor


print (soma)
print ('---')

# Realizando checagem de tipos de elementos da lista.
l15 = ['string', True, 10, -20.5]
for elem in l15:
    print(f'O item {elem} é {type(elem)}.')
print ('---')

