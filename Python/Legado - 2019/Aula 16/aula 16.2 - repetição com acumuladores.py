'''
while / else
contadores
acumuladores
'''
# Abaixo temos exemplos de contadores.
counter = 0
while counter <= 10:
    print(counter)
    counter += 1
print ('Fim!')
print('---')

counter2 = 50
while counter2 <= 100:
    print(counter2)
    counter2 += 1
print ('Fim!')
print('---')

# Abaixo exemplos de acumuladores e uso de else.
counter3 = 1
accumulator = 1  # aqui iremos acumular o valor da variável.

while counter3 <= 10:
    print(counter3, accumulator)

    accumulator = accumulator + counter3
    counter3 += 1
else:  # while permite o uso do else dentro do loop.
    print('Cheguei no else.')
print ('Fim!')
print('---')

# usando break
counter4 = 1
accumulator2 = 1

while counter4 <= 10:
    print(counter4, accumulator2)

    if counter4 > 5:  # aqui mostra que se o contador for maior que 5 deve parar a execução do código.
        break         # E não executará o else, mas saltará para o print ('Fim!')

    accumulator2 = accumulator2 + counter4
    counter4 += 1
else:
    print('Cheguei no else.')
print ('Fim!')
print('---')
