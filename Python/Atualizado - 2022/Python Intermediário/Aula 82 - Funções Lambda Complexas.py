'''
fuções x lambda
'''

def executa (funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# criando uma lambda para soma
a = float(input('Digite um números: '))
b = float(input('Digite outro números: '))
p(
    executa(
        lambda x, y: x + y,
        a, b
    )
)
p('---')

# lambda com multiplicação
duplica = executa(
    lambda m: lambda n: n * m,
    a
)
p(duplica(b))
p('---')

# passando args para lambda
p(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,9
    )
)
p('---')