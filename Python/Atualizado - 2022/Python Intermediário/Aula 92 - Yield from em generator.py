# Yield from
def gen1():
    print("Começou Gen1")
    yield 1
    yield 2
    yield 3
    yield 4
    print("Acabou Gen1")

def gen3():
    print("Começou Gen3")
    yield 10
    yield 20
    yield 30
    yield 40
    print("Acabou Gen3")

def gen2(gen):
    print("Começou Gen2")
    yield from gen()
    yield 5
    yield 6
    yield 7
    yield 8
    print("Acabou Gen2")



g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)
print('---')

for numero in g2:
    print(numero)
print('---')

# ou

def gen1():
    print("Começou Gen1")
    yield 1
    yield 2
    yield 3
    yield 4
    print("Acabou Gen1")

def gen3():
    print("Começou Gen3")
    yield 10
    yield 20
    yield 30
    yield 40
    print("Acabou Gen3")

def gen2(gen):
    print("Começou Gen2")
    yield from gen
    yield 5
    yield 6
    yield 7
    yield 8
    print("Acabou Gen2")



g1 = gen2(gen1())
g2 = gen2(gen3())

for numero in g1:
    print(numero)
print('---')

for numero in g2:
    print(numero)
print('---')

# condicional dentro do gen2

def gen1():
    print("Começou Gen1")
    yield 1
    yield 2
    yield 3
    yield 4
    print("Acabou Gen1")

def gen3():
    print("Começou Gen3")
    yield 10
    yield 20
    yield 30
    yield 40
    print("Acabou Gen3")

def gen2(gen=None):
    print("Começou Gen2")
    if gen is not None:
        yield from gen()
    yield 5
    yield 6
    yield 7
    yield 8
    print("Acabou Gen2")



g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()

for numero in g1:
    print(numero)
print("Fim do g1")
print('---')

for numero in g2:
    print(numero)
print("Fim do g2")
print('---')

for numero in g3:
    print(numero)
print("Fim do g3")
print('---')
