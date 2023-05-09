'''
a função input faz a captura da entrada de dados.
'''
from datetime import datetime
# O input sempre converte para str
name = input ("Qual o seu nome? ")
age = input("Qual a sua idade? ")
# age = int(input("Qual a sua idade? ")
# currentYear = datetime.now().year
# birthyear = currentYear - age

birthyear = 2019 - int(age)

print (f'O usuário digitou {name} '  # A função input por padrão retorna o formato string
       f'e o tipo da variável é {type(name)}')
print (f'{name} tem {age} anos.'
       f'{name} nasceu em {birthyear}')
