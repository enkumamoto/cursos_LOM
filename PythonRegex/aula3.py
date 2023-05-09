# Meta caracteres: . ^ $ ( )
# * representa 0 ou n
# + representa 1 ou n
# ? representa 0 ou 1
# ()+ [a-zA-Z0-9]
# {n} especificamente a quantidade desejada
# {min, max}
## {n, } de n ao max
## {, n} ate o valor de n
## {x,n} de x ate n


import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jão
'''

print(re.findall(r'jOãO', texto, flags=re.I)) # acha os dois joao, mas nao o ultimo
print("---")

print(re.findall(r'jo+ão+', texto, flags=re.I)) # o quantificador busca o que esta a esquerda dele
print("---")

# substituindo palavras dentro do texto
print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I)) # So altera a saida
print("---")

print(re.sub(r'jo*ão*', 'Felipe', texto, flags=re.I)) # So altera a saida
print("---")

print(re.sub(r'jo?ão*', 'Felipe', texto, flags=re.I)) # So altera a saida mas mantem o Joooooooooãooooooo
print("---")

# exemplificando a captura de quantidade especifica de repeticao
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
print("---")

# exemplificando range
texto2 = 'ele ama ser amado'

print(re.findall(r'ama[do]{0,2}', texto2, flags=re.I))