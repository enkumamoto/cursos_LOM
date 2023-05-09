'''
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente

Quando usados o output sem´re será um valor booleano.
'''
# No caso 2 é um valor literal e não pode reconfigura-lo, por exemplo não pode-se dizer que 2 é igual a 4.
# Lembre-se, quando usa um sinal de igual (=) está afirmando algo, quando usa dois sinais de igual ( == )
# está perguntando algo, nisso o python só pode responder se é True ou False.

print (2 == 2)
print ('---')

# Vamos dizer que há uma necessidade de checagem de números inteiros
num_1 = 2
num_2 = 2
# num_2 = '2'  # Python retorna falso caso tente checar inteiros com strings

exp = (num_1 == num_2)  # Aqui é está "afirmando que quer a resposta dapergunta"
print(exp)
print ('---')

# Vamos dizer que há uma necessidade de checagem de números inteiros é maior que:
num_1 = 3
num_2 = 2

exp = (num_1 > num_2)  # Aqui é está "afirmando que quer a resposta de maior que"
print(exp)
print ('---')

# Vamos dizer que há uma necessidade de checagem de números inteiros é maior que ou igual:
num_1 = 2
num_2 = 2

exp = (num_1 >= num_2)  # Aqui é está "afirmando que quer a resposta maior que ou igual"
print(exp)
print ('---')

# Vamos dizer que há uma necessidade de checagem de números inteiros é menor que :
num_1 = 3
num_2 = 2

exp = (num_1 < num_2)  # Aqui é está "afirmando que quer a resposta menor que"
print(exp)
print ('---')

# Vamos dizer que há uma necessidade de checagem de números inteiros é menor que ou igual:
num_1 = 2
num_2 = 2

exp = (num_1 <= num_2)  # Aqui é está "afirmando que quer a resposta menor que ou igual"
print(exp)
print ('---')

# no caso de diferente ( != ) e igualdade ( == ) pode checar strings
var_1 = 'Eiji'
var_2 = 'Kumamoto'

exp = (var_1 != var_2)  # Neste caso retorna True por que as duas variáveis tem valores diferentes
print (exp)
print ('---')

var_1 = 'Eiji'
var_2 = 'Kumamoto'

exp = (var_1 == var_2)  # Neste caso retorna False por que as duas variáveis tem valores diferentes
print (exp)
print ('---')
