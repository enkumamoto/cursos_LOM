# isinstance = para verificar o tipo do objeto

import os

lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Eiji'},
]

# as boas práticas dizem que listas devem ser específicas, 
# lista só para números, só para nomes, etc. 
# Misturar dados diferentes na mesma lista 
# podem causar problemas futuros
print("Exemplo 1")
for item in lista:
    print(item, isinstance(item, set))
    print('---')
print('---')

# também pode-se realizar checagem por tipo de classe
print("Exemplo 2")
for item in lista:
    if isinstance(item, set): # checando se há um set na lista
        print(item, isinstance(item, set))
        print('---')
print('---')

# ainda usando o exemplo acima, vamos usar o .add para adicionar mais um número no set
print("Exemplo 3")
for item in lista:
    if isinstance(item, set): # checando se há um set na lista
        print("SET")
        item.add(5) # adicionando o número 5 ao set
        print(item, isinstance(item, set))
        print('---')
        os.system("sleep 5")
        os.system("clear")

# checando str
    elif isinstance(item, str):
        print("STR")
        print(item.upper()) # deixando a str maiúscula
        os.system("sleep 5")
        os.system("clear")
        print('---')

# checagem de vários tipos numéricos
    elif isinstance(item, (int, float)): # realizando checagem
        print("NÚMERO")
        print(item, item * 2) # retornando os valores e os mesmos valores multiplicados por 2
        os.system("sleep 5")
        os.system("clear")
        print('---')
    
# outros
    else:
        print("OUTROS")
        print(item)
print('---')