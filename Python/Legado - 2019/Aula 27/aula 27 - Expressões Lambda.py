# Uma função comum para multiplicar dois números
def func(arg, arg2):
    return arg * arg2
var = func(2,2)
print (var)
print('---')

# com experessões lambda pode realizar a mesma coisa desta forma
a = lambda x, y: x * y
print(a(4,2))
print('---')

# Exemplo:
lista = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]
# ordenação de itens usando def
# def func(item):  # cria-se uma função para ordenar os itens por valor
#     return item[1]  #busca item 1
# lista.sort(key=func)  # e listará do valor menor ao maior. caso queira
                        # apresentar do maior para o menor basta acrescentar
                        # ',reverse=True'

# ordenação de lista usando lambda
lista.sort(key=lambda item: item[1])  # fará a mesma coisa que a função acima
print (lista)
print('---')
# ou
print(sorted(lista, key=lambda i: i[0],reverse=True))
print('---')