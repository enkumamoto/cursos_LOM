# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

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

print(re.findall(r'João|Maria', texto)) # aqui retorna uma lista com João ou Maria. cuidado com o espaço, isso pode alterar a ação do regex
print("---")

# caso adicione outro valor a busca, o regex buscará as palavras na sequência do texto
print(re.findall(r'João|Maria|adultos', texto))
print("---")

# exemplificando o .
print(re.findall(r'João|Maria|ad.....', texto))
print("---")

# exemplificando um conjunto de caracteres
print(re.findall(r'[Jj]oão|[Mm]aria', texto)) # por exemplo, a palavra joão com o J ou j restornará na busca
print("---")

# também pode-se usar range
print(re.findall(r'[A-Za-z]aria', texto)) # também aceita range numérico
print("---")

# uso de flags IGNORECASE
print(re.findall(r'jOãO|mAriA', texto, flags=re.IGNORECASE)) # com o IGNORECASE, ou simplesmente re.i, para ignorar maúsculo ou minúsculo
print("---")