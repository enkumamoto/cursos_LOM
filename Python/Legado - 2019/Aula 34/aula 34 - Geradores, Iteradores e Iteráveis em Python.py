'''
O que são iteráveis? Basicamente e a grosso modo, iteráveis em python são todos os objetos que implementam o método
__getitem__ ou __iter__. Beleza, vamos partir do simples. Quase todos os tipos de dados em python são iteráveis, por
exemplo: listas, strings, tuplas, dicionários, conjuntos, etc...

Um iterador de sequência, trabalha com uma sequência arbitrária que suporta o método __getitem__(). O segundo funciona
com um objeto que pode ser chamado e um valor de sentinela, chamando o que pode ser chamado para cada item na sequência
e finalizando a iteração quando o valor de sentinela é retornado.

Os geradores em Python são uma maneira simples de criar um objeto iterável sem a necessidade de construí-lo dentro de
uma classe. De forma bem resumida, um objeto iterável consiste em um conjunto finito de dados¹ cujo conteúdo é tratado
(ou iterado, dah!) um elemento por vez, iniciando do primeiro e seguindo até o último, quando a iteração é terminada.

(¹) Também é possível produzir geradores que contém séries infinitas de dados.
'''

# listaé um objeto iterável, abaixo há uma linha de comando onde confirma-se
lista = [0, 1, 2, 3, 4, 5]
print(lista)
print(hasattr(lista, '__iter__'))
print ('---')

# string é iteráveis.
lista2 = 'string'
print(lista2)
print(hasattr(lista2, '__iter__'))
print ('---')

# Já valores com números inteiros não são iteráveis.
lista3 = 1234
print(lista3)
print(hasattr(lista3, '__iter__'))
print ('---')

# O for é um iterador, vamos confirmar
lista = iter(lista) # Aqui converteu-se a lista para iterável
for v in lista:
    print(v)
    print(hasattr(lista, '__next__'))  # Usando o método __next__ para confirmar como iterador
print ('---')

# Uma outra forma de usar iterador
lista4 = [0, 1, 2, 3, 4, 5]
lista4 = iter(lista4)
print(next(lista4))
print(hasattr(lista4, '__next__'))
print ('---')

# Geradores
import sys
lista5 = list(range(10))  # Desta forma geraremos uma lista de 0 a 9
print(lista5)
print ('---')

# mas se usarmos da forma abaixo, mostrará quanto é o consumo de memória em bytes
lista6 = list(range(10000))  # se colocar mais zeros para aumentar o tamanho do número também aumentará a quantidade de bytes
print(lista6)
print(sys.getsizeof(lista6))
print ('---')

# Entenda que quando usamos geradores no python, normalmente os valores são salvos na memória, que não é o ideal.
# O correto é usar de forma otimizada, usando os geradores para usar os valores gerados sem salva=los na memória.
# Por exemplo:
import time
def gera():
    r = []  # r é igual a array
    for n in range(100): # gera valores um valor sequencial (0-99) a cada passagem
        r.append(n)  # acrescenta o valor ao array
        time.sleep(0.1)  #pede pro programa dormir por uma faixa de tenpo
    return (r)  # retorna ao r

g = gera()  #chamada da função gera
for v in g:  # laço for para criar a lista
    print(v) # apresenta todos os valores de uma vez.
print ('---')

# Editando a função acima para transforma-la em função geradora
def gerador():
#    r = []  # r é igual a array, mas numa função geradora passa a ser desnecessário
    for n in range(100): # gera valores um valor sequencial (0-99) a cada passagem
        yield n  # o yield suspende a execução naquele ponto, salva seu contexto e retorna para o chamador, juntamente com qualquer valor na lista
        time.sleep(0.1)  #pede pro programa dormir por uma faixa de tenpo
#    return (r)  # retorna ao r, mas com o yield esta parte perde sentido.

q = gerador()  #chamada da função gera
# print(g)  # apresentará uma saída de um objeto gerador e o ponto na memória onde foi salvo o valor.
#print(hasattr(g, '__iter__'))  # pode usar as formas citadas ou print(next(g))
#print(hasattr(g, '__next__'))
for t in q:  # laço for para criar a lista
    print(t)  # e apresentará um número por vez.
print('---')

# mais uma forma para função geradora sem laço for
def geradores():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

h = geradores()
#print(next(g))  # a função next a cada chamada retornará o valor
#print(next(g))
#print(next(g))
#print(next(g))  # cada print chamará um dos valores acima, mas quando chamar a quarta vez, retornará um erro.
for f in h:
    print(f)
print('---')
