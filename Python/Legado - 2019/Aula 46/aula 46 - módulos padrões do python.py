# Módulos padrão do python:
# Módulos são arquivos.py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem
#Veja todos os módulos padrão do python em:
# https://docs.python.org/3.9/py-modindex.html

#por exemplo, o usuário que saber em qual plataforma o python está rodando:
import sys
print(sys.platform)
print("---")

'''Caso queira simplesmente importar algo específico do módulo pode fazer da forma abaixo:
from sys import plataform
print(plataform)

ou pode "apelidar" a função do módulo:
from sys import plataform as SO
print(SO)
'''

# para gerar números aleatório
import random
print(random.randint(0,10))
print("---")

#utilizando o módulo num laço for
for i in range(10):
    print(random.randint(0, 10))
print("---")

# atenção quando escrever o código para não criar uma função e sobre escrever uma função do módulo
#aqui importou-se únicamente a função randint
from random import randint

def randint (*args): # neste ponto o python entende que a função randint está aqui e deve sobrescrever a do módulo
    return "hahaha"

for i in range(10):
    print(randint(0, 10)) # ao chegar neste ponto, será "printado" 10xhahaha
print("---")

#abaixo uma correção da situação acima
from random import randint as rndint # colocando um aplelido a importação

def randint (*args): #mantém a função
    return "hahaha"

for i in range(10):
    print(rndint(0, 10)) #corrigindo o argumento dentro do print
print(randint()) # imprimi um hahaha
print("---")
