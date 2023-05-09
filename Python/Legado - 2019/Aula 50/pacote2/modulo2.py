# existe também a possibilidade de importa um módulo dentro de um outro módulo
from pacote1.modulo1 import variavel1
variavel2 = 'variavel2'

print(variavel1)

# se executar este arquivo teremos um erro, por que o python leva em consideração a hierarquia de diretório.
# com isso, o arquivo principal que está mais próximo da raiz conseguirar executar os módulos mas o próprio
# módulo sendo executado terá erro.