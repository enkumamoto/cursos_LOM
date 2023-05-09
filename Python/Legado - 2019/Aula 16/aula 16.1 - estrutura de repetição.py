'''
Laço ou loop while
utilizado para realizar ações enquanto
uma condição for verdadeira
'''
# Exemplo de looping infinito.
# while True:
#    name = input('Qual seu nome? ')
#    print (f'Olá {name}!')  #  Enquanto a condição for verdadeira o loop será executado mas não executará o próximo print.
# print ('Não será executada.')
# print('---')

# Exemplo de loop finito para contar até 10
x = 0
while x < 10:  # Aqui apresenta que enquanto o x for menor que 10, o código deve ser executado.
    print(x)
    x = x + 1  # Aqui o loop irá somar 1 ao valor de x para realizar nova checagem.
print ('Fim!')
print('---')

# Um exemplo de uso 'continue' de forma errada.
# x = 0
# while x < 10:  # Aqui apresenta que enquanto o x for menor que 10, o código deve ser executado.
#     if x == 3:  # Aqui ele checa quando o x for igual a 3
#         continue  # Como o x é igual a 3 o continue entra em loop infinito e não finaliza o programa
#     print(x)
#     x = x + 1  # Aqui o loop irá somar 1 ao valor de x para realizar nova checagem.
# print ('Fim!')
# print('---')

# Para solucionar o problema acima, o código deve ficar da seguinte forma.
x = 0
while x < 10:  # Aqui apresenta que enquanto o x for menor que 10, o código deve ser executado.
    if x == 3:
        x = x + 1  # Aqui voltará a atribuir valor ao x
        continue  # E saltará o número 3 mas continuará rodando o código.
    print(x)
    x = x + 1  # Aqui o loop irá somar 1 ao valor de x para realizar nova checagem.
print ('Fim!')
print('---')

x = 0
while x < 10:  # Aqui apresenta que enquanto o x for menor que 10, o código deve ser executado.
    if x == 3:
        x = x + 1  # Aqui voltará a atribuir valor ao x
        break  # Irá finalizar o código e saltará para o último print quando x for igual a 3.
    print(x)
    x = x + 1
print ('Fim!')
print('---')

# Criando valor estilo planilha com while usando X e Y. Por exemplo, criando uma planilha com 10 colunas
# e 5 linhas.
x = 0  # colunas
while x < 10:
    y = 0  # linhas

    while y < 5:
        print (f'X vale {x} e Y vale {y}.')
        y+= 1
    x += 1
print ('Fim!')
print('---')

# Exemplo de uso de while num programa chamado Calculadora.
while True:
    print ()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input ('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão')

# Aqui temos um break para conseguir sair do loop
    if sair == 's':
        break

# Para evitar erros, pode-se realizar checagem caso o usuário tente digitar algo que não seja um número
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(f'A resultado de {num_1} + {num_2} é:',(num_1 + num_2))
    elif operador == '-':
        print(f'A resultado de {num_1} - {num_2} é:',(num_1 - num_2))
    elif operador == '/':
        print(f'A resultado de {num_1} / {num_2} é:',(num_1 / num_2))
    elif operador == '*':
        print(f'A resultado de {num_1} * {num_2} é:',(num_1 * num_2))
    else:
        print('Operador inválido')
