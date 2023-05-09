'''
Funções usando *args e **kwargs
'''
def func(a1, a2, a3, a4, a5):  # função com argumentos
    print(a1,a2,a3,a4,a5)

func(1,2,3,4,5)
print('---')

def func(a1, a2, a3, a4, a5, nome=None, a6=None):  # caso adicione um argumento nomeado os argumentos seguintes deverão ser nomeados também
    print(a1,a2,a3,a4,a5, nome, a6)

func(1,2,3,4,5, nome='Eiji', a6='6')  # Aqui passa a nomeação do argumento. se não passa o nome para o argumento vai retornar None
print('---')

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1,a2,a3,a4,a5, nome, a6)
    return nome, a6  #retornará uma tupla na variável.

var = func(1,2,3,4,5, nome='Eiji', a6='6')  # pode-se colocar uma função como valor de uma variável
print (var[0], var[1])  # se executar sem o return na função retornará None. Também pode-se realizar acesso aos índices das tuplas
print('---')

# Acima recapitulamos o básico de função. agora focaremos em args e kwargs
# muitas vezes não se sabe quantos argumentos serão passados para a função, com isso usa-se o *args
def func(*args):
    print(args)

var = func()  # executando retorna valor nulo ou vazio.
print('---')

def func(*args):
    print(args)

lista = [1,2,3,4,5]  # pode-se criar uma lista e jogar alguns valores em variáveis.
n1, n2, *n = lista  # onde '*n' recebe o restante da lista.
print(n1,n2,n)  # aqui desempacota os dois primeiros valores para n1 e n2, e empacotando o restante da lista em n
print('---')

def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista, sep=';')  # será apresentado o desempacotamento da lista e o números serão separados por espaços. mas com o 'sep=' pode-se escolhe o separados a ser colocado entre os números.
print('---')

def func(*args):
    print(args)  # aqui apresenta os argumentos em um tupla
    print(args[0])  # acessando o primeiro valor da tupla
    print(args[-1])  # acessando o ultimo valor da tupla
    print(len(args))  # pode-se usar funções para verificar os args
func(1,2,3,4,5)
print('---')

# Tuplas são imutáveis.
def func(*args):
    args = list(args)  # mas fazendo um casting, consegue mudar o valor de um item da tupla. convertendo de tupla para lista
    args[0] = 20
    print (args)

func(1,2,3,4,5)
print('---')

def func (*args):
    for v in args:  # também pode-se trabalhar com tuplas dentro do for
        print (v)

func(1,2,3,4,5)
print('---')

def func (*args):
    # print (args[0])  # colocando o índice dentro de args, será apresentado a lista dentro da tupla
    print(args)   #não colocando o índice.

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
#func(lista, '6')  # aqui adiciona-se o item 6 a lista empacotada
func(*lista, *lista2)  # listas desempacotadas.
print('---')

def func (*args, **kwargs):  # kwargs são argumentos com palavras chaves
    print(args)   #não colocando o índice.
    print(kwargs['nome'], kwargs['sobrenome'])  #acessando kwargs

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='Eiji', sobrenome='Kumamoto')  # listas desempacotadas.
print('---')

# uma forma melhor de e mais limpa do uso de kwargs
def func (*args, **kwargs):
    print (args)

    nome = kwargs.get('nome')
    print (nome)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='Eiji', sobrenome='Kumamoto')
print('---')

# realizando checagem se foi enviado algum argumento dentro do código. (checando idade)
def func (*args, **kwargs):
    print (args)

    idade = kwargs.get('idade')

    if idade is not None:
        print (idade)
    else:
        print('Idade não existe.')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='Eiji', sobrenome='Kumamoto', idade=38)
print('---')

def func (*args, **kwargs):
    print (args)

    # idade = kwargs['idade']  # se a idade não estiver declarada retornará erro.

    idade = kwargs.get('idade')

    if idade is not None:
        print (idade)
    else:
        print('Idade não existe.')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

func(*lista, *lista2, nome='Eiji', sobrenome='Kumamoto',idade=38)
print('---')