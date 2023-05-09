'''
Sets em Python (conjuntos)
add(adiciona), update(atualiza), clear, discard
unio | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esqueda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

sets em python so suporta elementos únicos
O set usa chaves, então se não fizer da maneira correta, em vez de criar um set criará um dicionário. ou seja, não
recebe chave:valor e sim somente valor.
o set suporta elementos imutáveis e não tem índice
'''
s1 = {1,2,3,4,5,6}
print (s1)
print ('---')

# set são iteráveis
s1 = {1,2,3,4,5,6}
for v in s1:
    print (v)
print ('---')

# não pode criar set vazio, mas caso seja necessário, deve-se fazer da forma abaixo
s1 = set()
s1.add(1)  # a função .add adiciona elementos
s1.add(2)
s1.add(3)
s1.add((1,2,3,'Eiji'))

print (s1)
print ('---')

# descartando elementos do set
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add((1,2,3,'Eiji'))
print (s1)

s1.discard(2)  # a função .discard descarta elementos
print (s1)
print ('---')

# a função .update é similar a .add, porem a diferença é que ela é iterável e os elementos não tem posição fixa.
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add((1,2,3,'Eiji'))
print (s1)

s1.discard(2)
print (s1)

s1.update('Python')
print (s1)
print ('---')
# ainda dentro do update, os sets não aceitam elementos duplicados
s1 = set()
s1.update([1,2,3,4,5], {5,6,7,8,9})
print (s1)
print ('---')

# uma forma de usar sets é para eliminar elementos repetidos dentro de listas
l1 = [1,2,3,4,4,3,3,4,3,4,5,6,7,5,5,4,6,4,3,2,2,3,4,5,6,7,8,6,7,5,3,2,4,3,5,7,6,4,3,4, 'eiji', 'Eiji', 'Eiji']
l1 = set(l1)  # casting lista para set
print(l1)

l1 = list(l1)  # transformando de set para lista
print(l1)
print(l1[-1])
print ('---')

# utilizando union, intersection, difference e symmetric_difference
ss1 = {1,2,3,4,5}
ss2 = {1,2,3,4,5,6}

#união
ss3 = ss1 | ss2
print(ss3)

#interseção
ss3 = ss1 & ss2
print(ss3)

# diferença (o maior set menos o menor set)
ss3 = ss2 - ss1
print(ss3)  # apresentará somente o 6

ss1 = {1,2,3,4,5,7}
ss2 = {1,2,3,4,5,6}
ss3 = ss2 - ss1  # apresentará somente o 6 novamente
print(ss3)

ss1 = {1,2,3,4,5,7}
ss2 = {1,2,3,4,5,6}
ss3 = ss1 - ss2  # apresentará somente o 7
print(ss3)

# diferença simétrica(o maior set menos o menor set)
ss3 = ss2 ^ ss1
print(ss3)
print('---')

# checando booleanamente
# forma 1
l1 = ['eiji', 'ananda', 'duda', 'nina', 'junior']
l2 = ['junior', 'duda', 'duda', 'nina', 'ananda', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji']

l1 = set(l1)
l2 = set(l2)
print(l1 != l2)

# forma 2
l1 = ['eiji', 'ananda', 'duda', 'nina', 'junior']
l2 = ['junior', 'duda', 'duda', 'nina', 'ananda', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji']
l1 = list(set(l1))
l2 = list(set(l2))
print(l1 == l2)
print(l1,l2)

# forma 3
l1 = ['eiji', 'ananda', 'duda', 'nina', 'junior']
l2 = ['junior', 'duda', 'duda', 'nina', 'ananda', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji', 'eiji']

if set(l1) == set (l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')


print('---')