'''
Operador ternário
'''

# Normalmente o uso de condicionais é feito da forma abaixo
logged_user = False  # True = logado e False = não logado
if logged_user:
    msg = "Usuário logado!"
else:
    msg = "Usuário não está logado"
print(msg)
print('---')

# Mas o python aceita da forma abaixo também
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário não está logado.'
print (msg)
print('---')

# Caso tenha um sistema que seja para maiores de idade
age = 18
if age >= 18:
    print('Pode acessar')
else:
    print('Não pode acessar.')
print('---')

# ou
age = 17
major_age = (age >= 18)
msg = 'Pode acessar.' if major_age else 'Não pode acessar.'
print(msg)
print('---')

# ou com interação com usuário.
age = input("Digite sua idade: ")
if not age.isnumeric():
    print('Você precisa digitar só números.')
else:
    age = int(age)
    major_age = (age >= 18)
    msg = 'Pode acessar.' if major_age else 'Não pode acessar.'
    print(msg)
print('---')