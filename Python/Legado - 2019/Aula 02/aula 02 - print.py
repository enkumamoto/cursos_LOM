
# print (123456)
# print ('Eiji', 'Kumamoto')
print ('Eiji', 'Kumamoto', sep = '-')  # O 'sep=' é um argumento nomeado, e o print entende que o '-' é um separador
print()
print ('Eiji', 'Kumamoto', sep = '-', end=' # ')  # O 'end=' é um outro argumento nomeado, e o print entende que não deve quebrar a linha
print ('João', 'e', 'Maria', sep = '-', end='')  # Não há necessidade de colocar 'end=' na linha seguinte para ter o output desejado
print ()

'''
usando os argumentos nomeados, faça com que o output seja igual a 824.176.070-18
'''
print ('824', end='.')
print ('176', end='.')
print ('070', end='-')
print ('18', end='')
print()
print('ou')
print ('824', '176', '070', sep='.', end='-')
print('18')