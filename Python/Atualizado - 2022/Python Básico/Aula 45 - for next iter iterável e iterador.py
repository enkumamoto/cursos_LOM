
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
numeros = range(0, 100, 2)

for numero in numeros:
    print(numero)
print('---')

texto = iter("Eiji") # mostra onde o valor está alocado na memória
print(texto)
print('---')

# o next serve para entregar o próximo valor
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# print(next(texto)) # aqui ele levanta um erro por que acabou o valor do iterável
print('---')

# usando try e except para tratar erro
texto = "Eiji" #iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
print('---')

# usando o for
for letra in texto:
    print(letra)
print('---')