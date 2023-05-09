'''Calculadora com while'''

# print('Bem vindo a calculadora.')

# while True:
#     sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')

#     if sair is True:
#         print('Calculadora finalizada.')
#         break

#     elif sair is False:
#         number_1 = float(input('Digite o primeiro número: '))
#         number_2 = float(input('Digite o segundo número: '))
#         operacao = input('Escolha a operação que deseja realizar - [A]dição, [S]ubtração, [M]ultiplicação ou [D]ivisão: ').lower()

#         if operacao == 'a':
#             print('Você escolheu Adição.')
#             resultado = number_1 + number_2
#             print(f'Oresultado de {number_1} + {number_2} é {resultado}')
#             continue

#         elif operacao == 's':
#             print('Você escolheu Subtração.')
#             resultado = number_1 - number_2
#             print(f'Oresultado de {number_1} - {number_2} é {resultado}')
#             continue

#         elif operacao == 'm':
#             print('Você escolheu Multiplicação.')
#             resultado = number_1 * number_2
#             print(f'Oresultado de {number_1} - {number_2} é {resultado}')
#             continue

#         elif operacao == 'd':
#             print('Você escolheu Divisão.')
#             resultado = number_1 / number_2
#             print(f'Oresultado de {number_1} / {number_2} é {resultado}')
#             continue

'''Calculadora do professor'''
p('Bem vindo a calculadora.')

while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Escolha a operação que deseja realizar - "+-/*": ')

    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        p("Umdos números ou ambos digitados são inválidos.")
        continue
    
    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        p("Operador inválido.")
        continue
    elif len(operador) > 1:
        p('Digite apenas um operador')
        continue

    if operador == '+':
        p('Você escolheu Adição.')
        resultado = (num_1_float + num_2_float)
        p(f'O resultado de {num_1_float} + {num_2_float} é {resultado}')
    elif operador == '-':
        p('Você escolheu Subtração.')
        resultado = num_1_float - num_2_float
        p(f'O resultado de {num_1_float} - {num_2_float} é {resultado}')
    elif operador == '*':
            p('Você escolheu Multiplicação.')
            resultado = num_1_float * num_2_float
            p(f'O resultado de {num_1_float} - {num_2_float} é {resultado}')
    elif operador == '/':
            p('Você escolheu Divisão.')
            resultado = num_1_float / num_2_float
            p(f'O resultado de {num_1_float} / {num_2_float} é {resultado}')

    sair = input('Deseja sair? [S]im ou [N]ão: ').lower().startswith('s')

    if sair is True:
        p('Calculadora finalizada.')
        break