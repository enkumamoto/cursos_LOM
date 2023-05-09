'''
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
'''
print("Vamos Somar!")
n1 = int(input('Digite o primeiro número da soma: '))
n2 = int(input('Digite o segundo número da soma: '))
n3 = int(input('Digite o terceiro número da soma: '))
def soma(n1, n2, n3):
    return n1 + n2 + n3

somatorio = soma(n1, n2, n3)

if somatorio:
    print (f'O resultado da soma de {n1} mais {n2} mais {n3} é igual a: {somatorio}')
else:
    print ('Conta inválida')

print()
print('---\nResposta do Professor.')
print()
def soma1 (n4, n5, n6):
    print (n4 + n5 + n6)

soma1(1,1,1)
soma1(2,2,2)
soma1(1,2,3)