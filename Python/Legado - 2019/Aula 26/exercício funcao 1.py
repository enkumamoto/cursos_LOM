'''
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
'''
name = input('Digite seu nome: ')
def saudacao(saudacao='Olá,', nome=name):
    print(saudacao, nome+('!'))

saudacao()
print()
print('---\nResposta do Professor.')
print()
def saudacao(saudacao, nome):
    print(f'{saudacao}. {nome}')

saudacao('Olá', 'João')
saudacao('Oi', 'Maria')
saudacao('Hey', 'Zezinho')