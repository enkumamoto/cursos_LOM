'''
* Criar variáveis para nome (str) idade (int).
* altura (float) e peso (float) de uma pessoa
* Criar uma variável com o ano atual (int)
* Obter o ano de nascimento do cliente (baseado na idade e no ano atual)
* Obter IMC do cliente com 2 casa decimais (peso e altura do cliente)
* Exibir um texto com todos os valores na tela usando F-String (Com as chaves)
'''
from datetime import datetime
name = input('Digite seu nome completo: ')
age = int (input('Digite sua idade: '))
height = float (input('Digite a sua altura: '))
weight = float (input('Digite seu peso: '))

currentYear = datetime.now().year
birthyear = currentYear - age

imc = weight/ height ** 2
print ('{0} tem {1} anos, {5} de altura e pesa {2:.0f}Kg. \nO IMC de {0} é {4:.2f}. \n{0} nasceu em {3}.'. format(name, age, weight,birthyear,imc, height))
