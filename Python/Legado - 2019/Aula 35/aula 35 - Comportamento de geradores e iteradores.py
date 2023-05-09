'''Aula  complementar sobre iteradores e geradores'''

# listas, tuplas e strings = Sequencia = Iteráveis | o que quer dizer que sequências são iteráveis
nome = "Eiji Kumamoto"

for letra in nome:
    print(letra)

print ('#' * 80)

for letra in nome:
    print(letra)
print('---')

'''uma coisa que deve ficar clara é, o for converterá a string num iterador usando o módulo next até a string acabar. 
   ao chegar ao final da string ele levantará uma excessão "StopIteretion" e ai o programa para.'''

# Usando o módulo next dentro de um try e com o laço for após o except

iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))

except:
    pass
print ("CADÊ OS VALORES?")
for valor in iterador:
    print(valor)
print('---')

# O exemplo acima mostra que mesmo que a string não sendo iterada por completo, usando um laço for usará o que sobrou dela

nome = "Eiji Kumamoto"
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))  # a partir daqui o iterador será consumido
print(next(gerador))
print(next(gerador))
print(next(gerador))

print ('olha o for')

for letra in gerador:  # aqui consome o restante
    print(letra)

print ('consumiu mais?')

for letra in gerador:
    print(letra)
print('---')
# Se adicionar mais print(next(gerador)) o python retornará o erro de StopIteration