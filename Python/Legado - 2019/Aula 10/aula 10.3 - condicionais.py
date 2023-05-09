'''
Operadores Lógicos
and e or, not, in, e not in
'''

# realizando comparações
a = 2
b = 2
c = 1
print (a == b and b < c)  # Chegagem de duas expressões com 'and' ambas precisam ser verdadeiras ou falsas
# (Verdadeiro e Verdadeiro) = Verdadeiro
# (Verdadeiro e Falso) = Falso
print ('---')

print (a == b or b < c)  # Neste caso uma das duas expressões precisa ser verdadeira.
# (Verdadeiro ou Verdadeiro) = Verdadeiro
# (Verdadeiro ou Falso) = Verdadeiro
print ('---')

print (not a == b and not b < c)  # O not inverte a expressão de verdadeiro para falso
print ('---')

# Quero saber se há uma letra 'U' no nome.
name = 'Eiji Kumamoto'
if 'u' in name:  # Esta linha diz "Se U está em name, faça isso"
    print ('Existe a letra U no seu nome.')
else:
    print ('Não existe.')
print ('---')

name = 'Eiji Kumamoto'
if 'Kuma' not in name:  # Esta linha diz "Se asdas não está em name, faça isso"
    print ('Executei.')
else:
    print ('Existe o texto.')
