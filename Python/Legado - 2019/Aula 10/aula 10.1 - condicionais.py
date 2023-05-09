'''
Condições IF, ELIF e ELSE
'''
# Aqui
if True:
    print ('Verdadeiro.')
    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)
print ('---')

#Enquanto houver True, será dado output do print indentado
if True:
    print ('Verdadeiro.')
print('Essa expressão não é verdadeira.')
print ('---')

# Neste caso o else confirma o output para o False
if False:
    print ('Verdadeiro.')
else:
    print ('Não é verdadeiro.')
print ('---')

# Aqui o primeiro True será impresso mas o segundo não.
if False:
    print ('Verdadeiro.')
elif True:
    print ('Agora é verdadeiro.')
elif True:
    print ('Mais um verdadeiro.')
else:
    print ('Não é verdadeiro.')
print ('---')


# Aqui pode-se ser feito de duas formas: com o else ou colocando o último print no mesmo nével do emcadeamento das condições
if False:
    print ('Verdadeiro.')
elif False:
    print ('Agora é verdadeiro.')
elif False:
    print ('Mais um verdadeiro.')
else:
    print ('Não é verdadeiro.')
print ('---')

if False:
    print ('Verdadeiro.')
elif False:
    print ('Agora é verdadeiro.')
elif False:
    print ('Mais um verdadeiro.')
print ('Não é verdadeiro.')
print ('---')

'''
Uma outra coisa que deve ser lembrado é que pode-se colocar vários comandos dentro de uma condicional.
As indentações dentro de uma condicional são códigos filhos e só são executados quando a condicional for
verdadeira.
'''
if False:
    print ('Verdadeiro.')
    print ('teste teste2')
elif True:
    print ('Agora é verdadeiro.')
    name = input ("Qual seu nome? ")

    print (f'Seu nome é {name}!')
elif False:
    print ('Mais um verdadeiro.')
    print (22 +22)
else:
    print ('Não é verdadeiro.')
    print ('Olá!')
print ('---')
