'''
funções servem para reperti um bloco de código várias vezes.
'''
def funcao():
    print('Olá Mundo!')

funcao()
print('---')

# a função também pode ser montada de forma abaixo:
def funcao(msg):  # msg é uma variável
    print(msg)

funcao('Olar!')  # Se não colocar algum valor dentro dos parenteses para ser atribuido dentro da variável.
print('---')

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Eiji')
print('---')

name = input('Digite seu nome: ')
def saudacao(msg='Olá,', nome=name):  # as variáveis podem receber valor diretamente ou receber de outr variável.
    print(msg, nome)

saudacao()
print('---')

name = input('Digite seu nome: ')
def saudacao(msg='Olá,', nome=name):  # as variáveis podem receber valor diretamente ou receber de outr variável.
    print(msg, nome)
saudacao()
print('---')
