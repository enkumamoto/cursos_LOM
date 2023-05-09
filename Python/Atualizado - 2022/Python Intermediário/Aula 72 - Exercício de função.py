# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multi(*args):
    total = 1 # acumulador
    for numero in args:
        total *= numero
    return total

multiplica = multi(2,3,4)
p(multiplica)
p('---')
p(2*3*4)
p('---')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
p(dois_e_par)
p(par_impar(7))
p(par_impar(2387462785))
p(par_impar(238467528778))
p(par_impar(7283452843250))

p(par_impar is outro_par_impar)