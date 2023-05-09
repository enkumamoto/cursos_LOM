'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
print ('Bem vindo ao checador de números pares e impares.')

num1 = input('Digite um número inteiro: ')
if num1.isdigit():
    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'{num1} é um número par.')
    else:
        print(f'{num1} é um número ímpar.')

else:
    print (f'Foi digitado "{num1}". Isso não é um número.')


