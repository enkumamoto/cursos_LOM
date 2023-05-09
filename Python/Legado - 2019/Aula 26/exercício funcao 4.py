'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne Fizz, se o parâmetro for divisível por 5, retorne
Buzz. Se o parâmentro for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
'''
print("FizzBuzz!")
print('Checando se o número é divisível por 3 ou por 5 ou por 3 e 5.\nSe divisível por 3 exibirá FIZZ, por 5 BUZZ e pelos dois FIZZBUZZ!')
n1 = int(input('Digite o número desejado: '))

def fizzbuzz():
    if n1 % 3 == 0 and n1 % 5 == 0:
        print ("FizzBuzz!")

    elif n1 % 5 == 0:
        print ("Buzz!")

    elif n1 % 3 == 0:
         print ("Fizz!")

    else:
        print(f'O número {n1} não é divisível por 3 e 5.')

fizzbuzz()

print()
print('---\nResposta do Professor.')
print()

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f"FizzBuzz! {n} é divisível por 3 e 5. "
    elif n % 5 == 0:
        return f"Buzz! {n} é divisível por 5"
    elif n % 3 == 0:
        return f"Fizz! {n} é divisível por 3"
    else:
        return f'O número {n} não é divisível por 3 e 5.'

from  random import randint

for i in range(100):
    aleatorio = randint(0,99)
    print(fb(aleatorio))
