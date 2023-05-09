# podemos verificar o tempo de execução de função ou logs
# criaremos uma função decoradora para medir tempo de execução da função
from time import time
from time import sleep



def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao (*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f"\nA função{funcao.__name__} levou {tempo:.2f}ms para executar.")
        return resultado
    return interna

@velocidade
def demora():
    for i in range (10):
        print(i, end="")
#        sleep(1)

demora()

#deve-se ficar atento que quanto mais funções aninhadas mais complexo ficará o código.