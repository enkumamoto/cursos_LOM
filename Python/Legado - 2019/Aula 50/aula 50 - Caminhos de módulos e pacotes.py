'''
Nesta aula vamos trabalhar com modularização com python.
Neste caso, este arquivo será o arquivo principal do programa que usará os arquivos
modulo1 e modulo2
'''

# importando variáveis de outros módulos
from pacote1.modulo1 import variavel1
from pacote2.modulo2 import variavel2

print(variavel1) #se comentar esta linha, o print da variavel2 apresentará o print com resultado dos dois módulos
print(variavel2)
print('---')

# mas como o python sabe de onde inportar
import sys
print(sys.path) #este print apresentará todos os caminho onde o python busca por módulos