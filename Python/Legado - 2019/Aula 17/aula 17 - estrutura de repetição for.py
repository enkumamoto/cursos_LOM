'''
For in em Python
Iterando string com for
Função range (start = 0, stop, step=1)
'''

# Lembre-se que loopr for é para loops finítos
text = 'Python'

for n, letter in enumerate(text):  # a função enumerate enumera cara volta do laço for
    print(n, letter)

# exemplo com a função range
for n in range(10):  # pode-se colocar qualquer coisa como variável antes do in.
    print (n)

'''a função range ela começa por padrão em 0 mas caso queira iniciar apartir de outro
não tem problema basta codificar da forma abaixo'''
for n in range(5 ,10):
    print (n)

'''também dentro do range existe o step, ele faz com que o range realize saltos numa contagem
como por exemplo de 2 em 2 ou 3 em 3.
'''
for n in range(2 ,30, 2):
    print (n)

print('---')

for n in range(20, 10, -2):
    print (n)

# entao o range funciona desta forma: range(start, stop, step)

# abaixo dois exemplos para achar multiplos de um número. as duas formas fazem a mesma coisa.
for n in range(100):
    if n % 8 == 0:
        print(n)
print('---')

for n in range(0, 100, 8):
    print (n)
print('---')

# Pode usar laço for para interagir con string. com isso vamos usar a variável do inicio da aula.
new_string = ''
for letter in text:
    if letter == 't':
        new_string = new_string + letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
    else:
        new_string += letter
print(new_string)
print('---')
