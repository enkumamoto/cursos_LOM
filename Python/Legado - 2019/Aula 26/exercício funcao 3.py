'''
3 - Crie uma função que receba 2 numeros. O promeiro é um valor e o segundo é um percentual (ex. 10%). Retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo.
'''
print("Aumento Percentual!")
n1 = int(input('Digite o valor: '))
n2 = int(input('Digite quantos % de aumento: '))

def aumento(n1, n2):
    return n1 + (n1 * (n2 / 100))

percentual = aumento(n1,n2)

print(percentual)

print()
print('---\nResposta do Professor.')
print()

def au_percent(valor, percentual):
    return valor + (valor * percentual / 100)

ap = au_percent(12345, 55)
print(ap)
ap = au_percent(54321, 33)
print(ap)
ap = au_percent(9876543, 120)
print(ap)