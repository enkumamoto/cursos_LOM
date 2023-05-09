"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres
lista = [] # lista vazia
print(lista, type(lista))
print('---')

'''
Por exemplo, a lista é mutável, ou seja, ela pode modificar os 
caracteres (coisa que não pode ser feita na string). Assim 
também como ela suporta qualquer tipo de dado.
'''
#        0    1      2               3    4  cada índice positivo está separado por virgula
#       -5   -4     -3              -2   -1  os índices podem ser negativos também
lista = [123, True, 'Eiji Kumamoto', 1.2, []]
print(lista)
print(lista[2]) #dando print só no índice dois
print('---')

'''
como dito antes, listas são mutáveis, com isso trocaresmo o nome na string por outro.
'''
print(lista)
print(lista[2])
lista[-3] = "Ananda Seabra"
print(lista)
print(lista[2])
print('---')

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)
print('---')

'''
exemplificando o uso de métodos
'''
lista = [10, 20, 30, 40, 50, 60]
print(lista)
lista[2] = 300 # alterando o índice 2 da lista
print(lista)
del lista[2] # deletando o índice 2 da lista e o python reorganiza automaticamente os índices
print(lista)
print('---')

'''
se quer adicionar algo isando o append, o dado será incluido no final da lista
'''
lista = [10, 20, 30, 40]
print(lista)
numero = int(input('Digite um número inteiro para colocar na lista: '))
lista.append(numero)
print(lista)
print('---')

'''
se quer remover o último item da lista usandoi pop
'''
lista = [10, 20, 30, 40]
print(lista)
lista.append(50)
ultimo_numero = lista.pop() # o método pop removeu o último item da lista, no caso o 50
lista.append(60)
lista.append(70)
lista.append('BBB')
ultimo_numero = lista.pop() # o pop também remove strings
print('Removido o número', ultimo_numero)
print(lista)
print('---')

# o pop também pode receber o índice a ser deletado, basta declarar o índece dentro do pop.

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
print(lista)
lista.append('Eiji') # adicionando uma string no final da lista
print(f'O item {lista[4]} foi adicionado.')
nome  = lista.pop() # nome é o último item da lista
print(f'Removido: {nome}')
print('---')

'''
Vamos dizer que não saiba qual é o último item da lista e precisa usar o método del
'''
lista.append(1233) # adicionando uma string no final da lista
print(f'O item {lista[4]} foi adicionado.')
print(lista)
def numero():
     del lista[-1]
print(f'O item {numero()} foi adicionado.')
print(lista)
print('---')

'''
usando o insert para adicionar algum dado em alguma posição da lista.
'''
print(lista)
lista.insert(0, 5) # significa que estou adicionando  o dado cinco no índice zero (ou seja a primeira posição)
print(f'O item {lista[0]} foi adicionado.')
print(lista)
print('---')

'''
se usar um insert com um índice alto, como 100 por exemplo, funcionará 
(mesmo que a lista contenha 4 itens), porém se tentar acessar este 
índice o python acusa erro. mas se acessar o item na última posição 
(usando -1 ou 4 (no caso)), o python retornará o item adicionado
'''
print(lista)
lista.insert(100, 5)
print(f'O item {lista[0]} foi adicionado.')
print(lista)
try: # colocado um try e except para o programa receber o erro e não parar
    print(lista[100]) # aqui apresentará erro 
    print('---')
except:
    print(lista[-1]) # já aqui retorna o item
    print('---')

'''
é extremamente normal trabalhar com mais de uma lista em python, mas 
deve-se ficar atento em como usar essas várias listas
'''
# unindo listas
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # teremos a união das listas e não a soma delas e assim extendendo a lista
print(f'A união da lista_a com a lista_b é: {lista_c}')
print('---')

'''
usando o método extend. com o código abaixo vemos que usar o extend na lista_a com 
a lista_b e pedir o print da lista_d, o que acontecerá é um retorno de None.
Isso por que a método trabalhará com a lista_a. a grosso modo, é como a lista_b 
fosse uma extensão da a e que retorna o resultado é a lista_a.
'''
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) 
print(f'A união da lista_a com a lista_b é: {lista_d}')
print('---')

'''
para o código retornar a informação que queremos deve ficar assim
'''
ista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) 
print(f'A concatenação da lista_a com a lista_b é: {lista_c}')
print(f'Quando usamos "lista_a.extend(lista_b)" temos o retorno: {lista_a}')
print('---')

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
nome = "Eiji" # este valor é apontado para um ID de memória
noutra_variavel = nome # esta variável apontar para o ID de memória da variável anterior
nome = "Ananda" # esta variável apontar para um novo ID de memória
print(nome)
print(noutra_variavel)
print('---')

'''
agora vamos realizar umas modificações relacionadas as listas
'''
lista_a = ['Eiji', 'Ananda']
lista_b = lista_a # aqui afirmamos que a lista_b recebe os valores da lista_a
print(lista_b)

lista_a[0] = 'Junior' # agora dizemos que o item 0 da lista_a deve ser trocado
print(lista_b)
print('---')

'''
mas vamos dizer que não quer modificar a lista_b que contém os valores da lista_a
'''
lista_a = ['Eiji', 'Ananda']
lista_b = lista_a.copy() #aqui o método copy preserva os valores sem alterar (no caso apontando para outro ID de memória)
print(f'A lista_b tem os valores copiados da lista_a: {lista_b} vs {lista_a}')

lista_a[0] = 'Junior' # agora dizemos que o item 0 da lista_a deve ser trocado sem modificar a lista_b
print(f'A lista_a foi modificada: {lista_a}')
print(f'A lista_b não foi modificada: {lista_b}')
print('---')

'''
uso de for in com lista.
no caso a gente usa a lista como iterável
'''
lista = ['Eiji', 'Ananda', 'Duda']

for nome in lista:
    print (nome)