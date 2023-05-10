# \w ---> [a-zA-Z0-9À-ú_]
# flags=re.A ---> re.ASCII
# \W ---> [^a-zA-Z0-9_]
# \d ---> [0-9]
# \D ---> [^0-9]
# \s ---> [\r\n\f\n\t]
# \b encontra a borda
# \B encontra nao borda


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

# print(re.findall(r'[a-z]+',texto, flags=re.I)) #captura todas as palavras nao acentuadas e ignorar o range de minusculas e numeros
# print('---')

# print(re.findall(r'[a-zA-Z]+',texto)) #captura todas as palavras nao acentuadas e ignorar o range de minusculas sem flags e numeros
# print('---')

# print(re.findall(r'[a-zA-ZÀ-ú]+',texto)) #captura todas as palavras e ignorar o range de minusculas
# print('---')

# # a ultima expressao acima pode ser mais curta usando o \w
# print(re.findall(r'\w+',texto)) # \w eh um shorthands
# print('---')

# print(re.findall(r'\w+',texto, flags=re.A))
# print('---')

# print(re.findall(r'\W+',texto))
# print('---')

# print(re.findall(r'\W+',texto, flags=re.A))
# print('---')

# print(re.findall(r'\d+',texto))
# print('---')

# print(re.findall(r'\D+',texto))

# print(re.findall(r'\s+',texto))
# print('---')

# print(re.findall(r'\S+',texto))
# print('---')

# print(re.findall(r'\be\w+',texto,flags=re.I))
# print('---')

# print(re.findall(r'\w+e\b',texto,flags=re.I))
# print('---')

# print(re.findall(r'\b\w{4}\b',texto,flags=re.I))
# print('---')

texto = '''
192.124.542-34
235.456.236.86
345.567.234.89
'''

print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', texto))