# Meta caracteres: . ^ $ ( )
# * representa 0 ou n
# + representa 1 ou n
# ? representa 0 ou 1
# {n}
# {min, max}

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
'''

print(re.findall(r'jOãO', texto, flags=re.I)) # acha os dois joao, mas nao o ultimo
print("---")

print(re.findall(r'jo+ão', texto, flags=re.I))