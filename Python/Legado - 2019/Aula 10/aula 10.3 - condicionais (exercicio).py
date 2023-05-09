user = input('Nome de Usuário: ')
passwd = input ('Senha do Usuário: ')

user_db = 'eiji'
user_pwd = '123456'

if user_db == user and user_pwd == passwd:
    print ('Seja bem vindo!')
else:
    print ('Usuário ou senha inválidos.')
