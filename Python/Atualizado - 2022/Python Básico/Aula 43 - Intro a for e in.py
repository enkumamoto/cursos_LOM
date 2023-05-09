'''Uso do for e do in'''

texto = 'Python'

i = 0

tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])

    i = i + 1

print('Acabou')
print('---')

texto = 'Python S2'

i = 0

tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)

    i = i + 1

print('Acabou')
print('---')

'''
não é comum usar while com "coisas' que se sabe quando termina, normalmente é usado para checar grandes conteúdos.
no caso abaixo, faremos uma validação de senha.
'''
senha_salva = '123456' # imagine que esta senha está numa base de dados de
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input (f'Sua senha {repeticoes}x: ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas.')
print('---')

'''
agora o uso de laço for, já que é melhor de trabalhar com iteráveis por que sabe-se quando ele acaba
perceba como o código é mais simples que usando while.
'''
texto = "Python"

for letra in texto:
    print(letra)

print('Acabou')
print('---')

'''
outro exemplo do uso do for
'''
texto = "Python"
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto +'*')
print('Acabou')
print('---')
