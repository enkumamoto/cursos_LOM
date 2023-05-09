"""
For + Range
range -> range(start, stop, step)
range é uma função iterável 
"""

#numeros = range(10) # se determinar um número dentro do range, significa que o range deve parar naquele numero, neste caso de 0 a 9
#numeros = range(5,10) # aqui se inicia em 5 e termina no 9
#numeros = range(5, 10, 2) # aqui se inicia em 5 e termina no 9 mas pulando de 2 em 2 números
numeros = range(0, -10, -1) # aqui se inicia em 0 e termina no -9 mas pulando

for numero in numeros:
    print(numero)
print('---')

'''exemplo: pegar os númeors pares de 0 a 100'''
numeros = range(0, 100, 2)
for numero in numeros:
    print(numero)
print('---')