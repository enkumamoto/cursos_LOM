# pass ou ... (ellipsis) são place holders, são palavras chaves que "seguram o lugar" para algo
# e escrever o que gostaria no bloco em um outro momento.

valor = True
if valor:
    print ('oi')
else:
    print ('tchau')
print ('---')

valor = False
if valor:
    print ('oi')
else:
    print ('tchau')
print ('---')

valor = True
if valor:
    pass
else:
    print ('tchau')
print ('---')

valor = True
if valor:
    ...
else:
    print ('tchau')
print ('---')
