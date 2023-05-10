# Meta caracteres: . ^ $ ( )
import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
print("---")

print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>', texto)) # quando se coloca um grupo entre parenteses o segundo grupo fica sendo referenciado pelo \1
print("---")

print(re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)', texto)) # retorna uma tupla com os dois grupos
print("---")

#usando como variavel
tags = re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)', texto)
for tag in tags:
    print(tag)
print('---')

# ou
for tag in tags:
    um, dois = tag
    print(um, dois)
print('---')

from pprint import pprint

pprint(tags)
print('---')

# criando outro grupo para reservar somente os textos
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

tags = re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2)',texto) #retorna o texto limpo sem marcacoes HTML
for tag in tags:
    um, dois, tres = tag
    pprint(tres)
print('---')

tags = re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>',texto)
pprint(tags)
print("---")

#testando com cpf
cpf = '934.675.235-13'
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}', cpf))
print('---')

#recriando usando sub
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 \3 \4', texto))