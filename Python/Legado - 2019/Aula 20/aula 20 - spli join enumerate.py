'''
Split, join e enumerate
split divide string
join junta uma lista
enumerate enumera elementos de uma lista /
'''
string = 'O Brasil é o país do futebol, o Brasil é penta.'

list = string.split(' ')  # esta linha diz que deve separar a string onde houver espaços.

print(list)
print('---')

string_2 = 'O Brasil é o país do futebol, o Brasil é penta.'
list_2 = string_2.split(',')
print(list_2)
print('---')

# caso queira iterar as duas listas:
for value in list:
    print(f'A palavra {value} apareceu {list.count(value)}x na frase.')
print('---')

# para uma checagem mais de talhada.
word = ''
check = 0
for value in list:
 times = list.count(value)

 if times > check:
     check = times
     word = value
print(f'A palavra que apareceu mais vezes é {word}({check}x)')
print('---')

# caso queira iterar as duas listas:
for value in list_2:
    print(value.strip().capitalize())  # aqui irá exibir as duas frases, retirando o espaço entre a virgula e deixando o 'o' da segunda frase em maiúculo.
print('---')

# usando o join
string_3 = 'O Brasil é penta.'
list_3 = string_3.split(' ')
string_t1 = ','.join(list_3)

print(string_3)
print(list_3)
print(string_t1)
print('---')

# usando o enumerate
string_4 = 'O Brasil é penta.'
list_4 = string_4.split(' ')

for indice, valor in enumerate(list_4):
    print(indice, valor)
    # ou
    #print(list_4[indice])
print('---')

# lista pode conter outras listas
listoflist = [
    [1,2],
    [3,4],
    [5,6],
]
for v in listoflist:
    print (v)
