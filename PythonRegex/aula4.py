## quantificadore grid e nao grid
# Meta caracteres: . ^ $ ( )
# * representa 0 ou n
# + representa 1 ou n
# ? representa 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[pdiv]{1,3}>', texto))
print("---")

print(re.findall(r'<[pdiv]{1,3}>.*', texto)) # aqui pega tudo
print("---")

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto)) # comportamento grid
print("---")

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto)) # modificando o comportamento para non grid
print("---")