# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

import os

def generator(n=0):
    return "Acabou"

gen = generator(n=0)
print(gen)
print('---')

# quando uma função é escrita, o return a finaliza, 
# no caso do generator dentro da função, podemos 
# pausar usando yield
def generator(n=0):
    yield 1 #pausa
    return "Acabou"

gen = generator(n=0)
#print(gen) # retorna um memory id
print(next(gen))    # chamando o próximo valor do generator, 
                    # só que se houver mais um pedido de interação, 
                    # o return da função é acionado e retorna o Acabou
print('---')

# exemplificando as pausas
def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma vez...')
    yield 3
    print('Terminando...')
    return "ACABOU!"

gen = generator(n=0)
print(next(gen))
print(next(gen)) # comentar esta linha teremos pausa no 1
print(next(gen)) # comentar esta linha teremos pausa no 2
#print(next(gen))# comentar esta linha teremos pausa no 3
os.system('sleep 2')
os.system('clear') 
print('---')
 
# usando laço for
def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Mais uma vez...')
    yield 3
    print('Terminando...')
    return "ACABOU!"

gen = generator(n=0)

for i in gen:
    print(i)
os.system('sleep 2')
os.system('clear') 
print('---')

# de uma outra forma 
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return "Acabou :D"
        

gen = generator() # o máximo pode ser mudado neste ponto

for i in gen:
    print(i)
# os.system('sleep 2')
# os.system('clear') 
print('---')