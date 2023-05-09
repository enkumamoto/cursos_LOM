'''
São utilizadas para:
1 - Otimização em termos de performance
2 - menos linhas escritas.
'''
# no exemplo abaixo a l2 copia l1 usando loop for
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
print (ex1)
print ('---')

# para criar uma lista onde se multiplica por 2 todos os itens da l1
ex2 = [v * 2 for v in l1]
print(ex2)
print ('---')

# criando tuplas em estilo coordenadas
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
print(ex3)
print ('---')

l2 = ['Eiji', 'Ananda', 'Duda']
ex4 = [v.replace('a', '@').upper() for v in l2]
print(ex4)
print ('---')

# usando com tuplas
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor'),
)
ex5 = [(x,y) for x,y in tupla]  # criando lista com tupla
print(ex5)
ex5 = [(y,x) for x,y in tupla]  # inversão dos itens
print(ex5)
ex5 = [(x,y) for x,y in tupla]
ex5 = dict(ex5)  # transformando em dicionário
print(ex5)
print ('---')

# criando lista com range e filtrando lista
l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]  # filtrando numeros divisíveis por 2
print(l3)
print (ex6)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]  # filtrando numeros divisíveis por 3 e por 8
ex7 = [v if v % 3 == 0 else 0 for v in l3]  # neste caso se o número não é divisível por 3 será trocado por 0
ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]  # uso de and (o or também pode ser usado da mesma forma).
print (ex6)
print (ex7)
print (ex8)
print ('---')
