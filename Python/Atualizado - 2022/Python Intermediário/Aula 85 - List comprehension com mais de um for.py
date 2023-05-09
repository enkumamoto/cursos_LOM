#list comprehension com vários for

# for dentro de for
lista = []

for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)
print('---')

# com list comprehension
lista = [
    x for x in range(3)
    for y in range(3)
]
print(lista)
print('---')