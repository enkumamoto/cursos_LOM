"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4 # *resto gera uma nova lista
p(x, y, resto)
p('---')

# def soma(x, y):
#     return x + y

def soma(*args): # neste caso todos os parâmentros passado para função serão armazenados em args
    p(args)

soma(1,2,3,4,5,6,7,8,9) # retornará uma tupla
p('---')

# lembrando que tuplas não podem ser alteradas, com isso pode-se convertes para lista
def soma(*args):
    args = list(args)
    p(args)

soma(1,2,3,4,5,6,7,8,9) # retornará uma lista
p('---')

# também pode-se usar laço for
def soma(*args):
    for numero in args:
        p(numero)

soma(1,2,3,4,5,6,7,8,9)
p('---')

# somando todos os números dados dentro dos parâmetros
def soma(*args):
    total = 0 # acumulador
    for numero in args:
        p(f'Total: {numero} + {total}')
        total += numero
        p('Total:', total)

soma(1,2,3,4,5,6,7,8,9)
p('---')

# fazendo uso do return
def soma(*args):
    total = 0 # acumulador
    for numero in args:
        total += numero
    return total

soma1 = soma(1,2,3,4,5,6,7,8,9)
p(soma1)
p('---')

# o python tem um módulo pronto (sum) que faz a mesma coisa que a afunção acima

numeros = 1,2,3,4,5,6,7,78,10
outra_soma = soma(*numeros) # com o * vira args sem * vira tupla
p(outra_soma)
p('---')

# usando o sum
numeros = 1,2,3,4,5,6,7,78,10
# print(sum(1,2,3,4,5,6,7,78,10)) # dessa forma gera erro, o sum() so suporta no máximo 2 argumentos
p(sum(numeros))
p('---')