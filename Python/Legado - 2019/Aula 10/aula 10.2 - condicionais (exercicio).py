
# Você precisa de um empréstimo mas o sistema do banco precisa checar se você é maior de 18 anos, como será a checagem?
name = input ('Qual o seu nome? ')
age = int (input('Qual a sua idade? '))
limit_age = 18
if age >= limit_age:
    print (f'{name}, você é de maior e pode requisitar um empréstimo.')
else:
    print (f'Desculpe-me {name}, mas você é de menor e não pode requisitar um empréstimo.')
print ('Obrigado por usar nossos serviços!')
print ('---')

# Você precisa de um empréstimo mas o sistema do banco só concede para pessoas entre 20 e 30 anos, como será a checagem?
name = input ('Qual o seu nome? ')
age = int (input('Qual a sua idade? '))
younger_age = 20
elder_age = 30
if age >= younger_age and age <= elder_age:
    print (f'{name}, você pode requisitar um empréstimo.')
else:
    print (f'Desculpe-me {name}, mas você não pode requisitar um empréstimo.')
print ('Obrigado por usar nossos serviços!')
print ('---')
