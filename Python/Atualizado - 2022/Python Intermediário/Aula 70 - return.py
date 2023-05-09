"""
Retorno de valores das funções (return)
"""
# já sabemos que print é uma função
p ('Eiji')
p('---')

# se colocar o print como valor de uma variável, a mesma imprime o valor
v = p ('Eiji')
p('---')

# se dermos um print na variável retornará None
v = p ('Eiji')
p(v) # isso acontece por que a variavel é um não valor
p (v is None) # confirmando a justificativa acima
p('---')

# o return retorna um resultado que pode enviado para qualquer variável dentro do programa
def soma(x, y):
    return x + y

soma1 = soma(2, 3)
soma2 = soma(4, 5)
p(soma1 + soma2)
p('---')