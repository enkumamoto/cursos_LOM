'''
operador or
'''
# Aqui temos uma checagem usando if
nome = input ('Qual o seu nome? ')
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')
print('---')

# com o or pode-se fazer desta forma.
nome = input ('Qual o seu nome? ')
print(nome or 'Você não digitou nada =(')
print('---')

# O or ele sempre vai parar na primeira condição verdadeira.
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = "Eiji"
variavel = a or b or c or d or e or f or g
print(variavel)
print('---')
