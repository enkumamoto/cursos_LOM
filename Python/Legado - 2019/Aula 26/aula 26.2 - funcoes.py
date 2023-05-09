'''
Funções e return
'''
def funcao(var):  # a variavel dentro dos parenteses da função é um parâmentro
    print(var)

funcao('Valor que eu quero')
print ('---')

def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')
print (variavel)  # retornará 'None' ou 'não valor'
print ('---')

def funcao(var):
    print (var)

variavel = funcao('Valor que eu quero')

if variavel:  # retornará valor False (booleano)
    print(variavel)
else:
    print('Nenhum Valor')
print ('---')

def funcao(var):
    return var  # retornará valor para var, um outro detalhe é que nada é executado após o return dentro da função.
    print ('Isso não será apresentado.')
    # return var  # Se coentado o return anterior e executar o código novamente, o print será exibido.

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum Valor')
print ('---')

print("Vamos dividir!")
n1 = int(input('Digite o dividendo: '))
n2 = int(input('Digite o divisor: '))
def divisao(n1, n2):  # criada uma função para divisão de dois números
    if n2 > 0:  # realizando checagem de divisor menor 0
        return n1 / n2  # o return apresentará o resultado da divisão entre n1 e n2

divide = divisao(n1,n2)  # passado os paramentros para divisão

if divide:
    print (f'O resultado da divisão de {n1} por {n2} é igual a: {divide}')
else:
    print ('Conta inválida')
print ('---')

print("Vamos dividir!")
n1 = int(input('Digite o dividendo: '))
n2 = int(input('Digite o divisor: '))
def divisao(n1, n2):  # criada uma função para divisão de dois números
    if n2 == 0:  # realizando checagem de divisor igual 0
        return  # aqui não realizará operação
    return n1 /n2  #mas aqui retorna a operação matemática

divide = divisao(n1,n2)  # passado os paramentros para divisão

if divide:
    print (f'O resultado da divisão de {n1} por {n2} é igual a: {divide}')
else:
    print ('Conta inválida')
print ('---')

def dumb():  # esta função é para checagem do tipo do dado
    return 1  # aqui pode colocar qualquer tipo de dado para entender melhor.
print(dumb(), type(dumb()))
print ('---')

def dumb():
    return True

var = dumb()
print(var, type(var))
print ('---')

def f2(var):
    print (var)

def dumb2():
    return f2

var2 = dumb2()
# print(type(var))
print (id(var2), id(f2))

if var2 == f2:
    print('var é igual a f')
else:
    print('Blaaaaaah')
print('---')

def f3(var):
    print (var)

def dumb3():
    return f3

var3 = dumb3() ('E colocar o valor aqui.')  # como o parametro foi declarado o id acaba mudando.
print (id(var3), id(f3))

if var3 == f3:
    print('var é igual a f')
else:
    print('Blaaaaaah')
print('---')

# Funções podem retornar tuplas
def dumb4():
    return('Eiji', 'Kumamoto', 'Neto')

var4 = dumb4()
print (var4[1], type(var4))