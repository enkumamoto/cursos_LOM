# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
#sys.exit() # essa função do módulo sys faz com que sai do programa, qualquer código após não será executado
print(123)
print('---')

# checando o kernel
print('Eu uso:')
print(sys.platform)
print('---')

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform
print(platform)
print('---')

# alias 1 - import nome_modulo as apelido
import sys as s # isto pode ser feito e não afetar a variável abaixo 
sys = "Eiji_OS" # mas é mais fácil mudar a variável
print(s.platform)
print(sys)
print('---')

# alias 2 - from nome_modulo import objeto as apelido
from sys import platform as pf
from sys import exit as ex
print(pf)
print('---')

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo