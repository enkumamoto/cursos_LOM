'''
count - itertools

a função count gera um contadore que é um iterador. diferente do range que é um gerador e não um contador
'''
from itertools import count  # importando o iterador

contador = count()  #criando variável com contador

print (next(contador))  #realizando contagem
print (next(contador))
print (next(contador))
print (next(contador))
print (next(contador))
print('---')

'''
Deve-se ter muito cuidado com o uso do count, pois usando dentro de um loop for sem um limitador se tornará um looping infinito
e fará o pc travar em algum ponto.
'''
contador = count()
for valor in contador:
    print(valor)
    if valor >= 10:
        break
print('---')

# uma coisa que o count permite é iniciar a contagem de um ponto que que queira
contador = count(start=5)  #aqui a contagem começará no número 5
for valor in contador:
    print(valor)
    if valor >= 10:
        break
print('---')

contador = count(start=5, step=2)  #aqui a contagem começará no número 5 mas pulando de 2 em 2
for valor in contador:
    print(valor)
    if valor >= 10:
        break
print('---')

contador = count(start=5, step=0.1)  #aqui a contagem começará no número 5 mas pulando de 0.1 em 0.1
for valor in contador:
    print(round(valor, 2))  #usando o round para arredondar o valor
    if valor >= 10:
        break
print('---')

# Obs.: Se caso o step recebe o valor negativo e o limitador recebe valor positivo, isso leva a um loop infinito
contador = count(start=5, step=-1)
for valor in contador:
    print(round(valor, 2))
    if valor >= 10 or valor <= -10:
        break
print('---')

# usnado o contador como um gerado de índice
contador = count(start=1)
lista = ['Ananda', 'Duda', 'Eiji', 'Nina']

lista = zip(contador, lista)
print(list(lista))
print('---')