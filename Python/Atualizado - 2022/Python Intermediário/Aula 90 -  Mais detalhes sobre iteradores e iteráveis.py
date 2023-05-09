# iterável: tem responsabilidade de reter os valores sequencialmente
# iterador: entregar um valor por vez
import os
import sys

iteravel = ['Eu', 'Tenho', '__iter__']
iterador = iteravel.__iter__() # tem __iter__ e __next__

# print(iterador(1)) # aqui o iterador não consegue saber nada
print(next(iterador)) # mas se usar o next funciona
print(next(iterador))
print(next(iterador))
# print(next(iterador)) # aqui vai retornar um StopIteration, pois não há com o que iterar
print('---')

# Generator são funções que sabem que pausar em determinada ocasião
# abaixo um exemplo de de um gerador que não é um generator
gerador = [n for n in range(10)] # lista
print(gerador)
os.system('sleep 2')
print('---')
os.system("clear")

# para ser um generator use parênteses em vez de colchetes
lista = [n for n in range(1000000)] # a lista está salva na memória e pode acessar via índice
gerador = (n for n in range(1000000)) # aqui o generator aguarda o pedido da sequência, mas não há índice

print(sys.getsizeof(lista)) # o getsizeof ve o tamanho do dado, em bytes, na memória
print(sys.getsizeof(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('---')

# usando num laço for
for n in gerador:
    print(n)
print('---')
os.system('sleep 2')
os.system("clear")