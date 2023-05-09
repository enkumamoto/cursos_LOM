'''
Lembrando que tuplas são imutáveis
Acesso aos itens é da mesma forma que nas listas '[x]'
'''
t1 = (1,2,3, 'a', 'Eiji')

print(t1[4])
print('---')

# Iterando lista
for v in t1:
    print (v)
print('---')

# fatiamento da tupla
print (t1[:2])
print('---')

# as tuplas podem ser criadas sem parenteses, o que deve-se fazer é colocar os itens separados por virgulas.
# e também pode concatena-las
t2 = 1,2,'Eiji',3,4,5,
t3 = 6,7,8,9,10
t4 = t2 + t3
print(t2, type(t2))

n1, n2, n3, *_, n6= t4
print (n3)
print('---')

# pode-se multiplicar a quantidade de visualização
t5 = t2 * 20
print (t5)
print('---')

# Tuplas são imutáveis, mas para alterar algum valor deve-se converter em lista.
t6 = (1,2,3,4,5,6,7,8,9)
t6 = list(t6)
t6[2] = 3000
print(t6, type(t6))
t6 = tuple(t6)
print(t6, type(t6))
print('---')