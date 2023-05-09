import math

PI = math.pi

def dobra_lista(lista): #esta função multiplica toda a lista por 2
    return [x*2 for x in lista]

def multiplica_lista(lista): #esta função multiplica os números da lista, exemplo: o primeiro índice será multiplicado pelo segundo, o resultado da primeira multiplicação será multiplicada pelo terceiro índice e assim por diante.
    r = 1
    for i in lista:
        r *= i
    return r

lista = [1,2,3,4,5]

# as partes abaixo forma comentadas por que elas retornam todos os prints dentro do aplicativo.py, porém
# foram usadas para demonstrar que as funções funcionam
# print(dobra_lista(lista))
# print(multiplica_lista(lista))
# print(PI)

# print(__name__) # deste ponto para cima, caso executado, retornará o __main__

# mas se quiser executar os prints de teste do módulo mas sem propagar basta usar um if:
if __name__ == "__main__":
    print(dobra_lista(lista))
    print(multiplica_lista(lista))
    print(PI)