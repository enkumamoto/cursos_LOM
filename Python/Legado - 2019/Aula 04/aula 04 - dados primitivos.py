# Tipos de dados

'''
str - string - Texto 'Assim' ou "Assim"
int - inteiro - 123456 0 -123456
float - real/ponto flutuante - 1.23
bool - booleano/lógico - True/False
'''
print ('Eiji',type('Eiji'))  # Aqui demonstra a classe 'type' apresentando a classe 'str'
print (10,type(10))  # Aqui demonstra a classe 'type' apresentando a classe 'int'
print (1.23,type(1.23))  # Aqui demonstra a classe 'type' apresentando a classe 'float'
print (10==10,type(10==10))  # Aqui demonstra a classe 'type' apresentando a classe 'bool'
print(bool(''))  # Retorna False

print ('Eiji',type('Eiji'), bool('Eiji'))  # Aqui converte a string eiji para booleano
print ('10', type('10'), type(int('10')))  # Aqui mostra um número como string mas convertido para inteiro

# Lembre-se que não pode converter texto e número com ponto flutuante para inteiro. Mas pode converter inteiro em float

name = input ('Digite seu nome: ')
age = input ('Digite sua idade: ')
height = input ('Digite sua altura: ')
major = False
print (name, type(name))
print (age, type(int(age)))
print (height, type(float(height)))

if major >= 18:
    print ('Você é maior de idade.',type(bool(major)))
else:
    print ('Você é menor de idade.',type(bool(major)))

