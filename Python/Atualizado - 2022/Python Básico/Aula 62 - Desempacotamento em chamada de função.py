'''
Desempacotamento em chamada de métodos e funções
'''
string = 'ABCD'
lista = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junior']
tupla = 'Python', 'é', 'legal'

a, b, c, *_ = lista # em caso de dúvidas, veja a aula 48
print(a, c)
print('---')

# é muito comum realizar desempacotamentos. no exemplo abaixo será usado as variáveis acima
for nome in lista:
    print (nome)
print('---')

for nome in lista:
    print(nome, end=' ') # o end colocará todos os nomes na mesma linha
print('')
print('---')

#ou pode usar o print da forma abaixo que terá o mesmo resultado do for acima
print(*lista)
print(*string)
print(*tupla)
print('---')

# usando com listas dentro de listas
salas = [
    # 0       # 1
    ['Maria', 'Helena',], # 0
    # 0
    ['Elaine',], # 1
    # 0
    ['Luiz', 'João','Eduarda', (0, 10, 20, 30, 40)], # 2
]
print(*salas) # desta forma apresenta-se linear
print(*salas, end='\n') # apresenta a quebra de linha, mas não muda a apresentação linear
print(*salas, sep='\n') # apresenta a quebra de linha, mas muda a apresentação
print('---')