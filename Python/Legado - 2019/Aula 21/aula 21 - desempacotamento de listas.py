'''
Desempacotamento de listas
'''
lista = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junior']

'''o desempacotamento funciona da seguinte forma: a quantidade de variáveis de
desempacotamento deve ser igual a quantidade de valores da lista. Se retirar
uma variável, retornará erro.
'''
n1, n2, n3, n4, n5 = lista
print(n2)
print ('---')

'''Caso não queira colocar varias variáveis para apontar cada índice basta usar
um '*' no inicio de uma variável. O '*' no início da variável quer dizer que 
esta variável é uma nova lista
'''
n1, *n = lista
print(n2)
print(n)
print ('---')
'''
Mas se colocar uma varivável n2 a nova lista será alterada
'''
n1, n2, *n = lista
print(n1, n2)
print(n)
print ('---')

'''
se quiser acessar o último item da lista, basta criar uma variável após a variável com asterisco.
ao mesmo tempo, este acesso retira o último item da lista e altera a lista '*n', neste caso 
retirando o número 100.
'''
lista2 = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junior',1,2,3,4,5,6,7,8,9,100]
n1, n2, *n, lv = lista2
print(n1, n2, lv)
print (n)
print ('---')

# ou desta forma, para 'pegar' os 3 últimos itens.
*n, n1, n2, n3= lista2
print(n1, n2, n3)
print (n)
print ('---')

# Por padrão o uso de "*_" significa que não usará a variavável dentro do código.
