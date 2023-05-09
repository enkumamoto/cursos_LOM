'''
Aqui usaremos o len. O len funciona com str e não com números (int e float) e nem com booleanos.
'''
user = input ('Digite seu usuário: ')
# Para checar a quantidade de caracteres e os tipos de caracteres que estão sendo lançados
caracter_qtd = len(user)  # Contará todos os caracteres (incluindo os espaços).
                          # Aqui retorna em inteiro e com isso pode-se realizar operações matemáticas.
# Suponha que queira que seu sistema não aceita usuário com menos de 6 caracteres:
if caracter_qtd < 6:
    print ('Nome de usuário precisa de no mínimo 6 caracteres.')
else:
    print ('Você foi cadastrado.')
print (user, caracter_qtd, type(caracter_qtd))
print ('----')

string1 = input('Digite seu nome: ')
string2 = input('Digite seu sobrenome: ')
print (f'A quantidade de caracteres digitados foi: {len(string1) + (string2.__len__())}')
