'''
Iterando strings com while - Exercício
'''

nome = 'Eiji Kumamoto Neto' 

indice = 0

novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    # novo_nome += (letra + '*') $esta forma também funciona.
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)