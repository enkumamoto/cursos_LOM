'''
escopo de variáveis em funções
'''

variavel = 'valor'  # a variável fora da função tem escopo global.

def func():
    print (variavel)

def func2():
    variavel = 'Outro Valor'  # já aqui está em escopo local (dentro da função).
    print (variavel)

func()
func2()
print (variavel)  # este print exibirá a variavel global.
print('---')

# Não é recomendado o uso de variável global dentro da função, pois pode gerar comportamento
# estranho dentro do programa, mas caso seja necessário usar uma variável global dentro da
# função deve-se declarar 'global varivael'

# Exemplo de como manipular variável global sem alterar a variável original
variavel = 'valor'  # a variável global.

def func():
    print (variavel)

def func2(arg=None):
    arg = arg.replace('v', 'c')  # aqui a função mudará a letra v pela letra c
    return arg  # preferível uso de argumentos e parametro em vez de variável global.

func()
outra_variavel = func2(arg = variavel)  # aqui chamará a variável global e realiza alteração do valor
print (outra_variavel)
print('---')

# variavel = 'valor'  # a variável global.
#
# def func():
#     print (variavel)  # neste caso o pyhton retorna erro. o erro diz que a função está tentando usar
#     variavel = 12345  # uma variável antes dela ser criada (configurada).
#     print(variavel)
#
# func()
