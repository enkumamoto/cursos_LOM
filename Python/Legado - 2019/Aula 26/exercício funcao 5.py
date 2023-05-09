'''
5 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
'''
def funcao1():
    var1 = 123
    return var1
def funcao2(arg):
    print (arg)

var = funcao1()
funcao2(var)

print()
print('---\nResposta do Professor.')
print()

def ola_mundo():
    return 'Olá Mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)