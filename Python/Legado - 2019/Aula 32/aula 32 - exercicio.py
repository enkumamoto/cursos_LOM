'''
Separe o valor da string em vários grupos de 0-9 e que o retorno final seja 'grupo.grupo...'
'''
string = '012345678901234567890123456789012345678901234567890123456789'

n = 10
lista = [string [i:i+10] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)