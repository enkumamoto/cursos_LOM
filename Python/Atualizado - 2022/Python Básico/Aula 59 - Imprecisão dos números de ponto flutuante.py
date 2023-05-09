"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
# lembre-se python não reconhece virgula em números quebrados
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # aqui o resultado será 0.799...
print('---')
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(f'{numero_3:.2f}') # já aqui será arredondado para 0.80. lembre-se aqui se formata um número que é uma string e não im inteiro.
print('---')

''' o python permite essas formatações numéricas para facilitar, 
mas também possui módulos nativos para isso, 
como por exemplo o round que faz o mesmo que .2f.
o formate (.<numero>f) formata o número decimal mostrando 0 no final.
já o round ignora a sequência de zeros após a casa decimal.
'''
numero_1 = 0.133
numero_2 = 0.71
numero_3 = numero_1 + numero_2
print(round(numero_3, 2)) # a virgula após a variável significa a quantidade de casas decimais a serem apresentadas
print('---')

# quando precisa-se calcular um número decimal muito grande é recomendado usar o módulo decimal
import decimal
numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
print('---')
'''
como pode ver, o número ficou muito grande, 
isso acontece porque o módula calcula 
precisamente os dois números. mas nada impede
de usar o round ou o .<numero>f.
uma coisa interessante é que o módulo decimal
"funciona melhor" com strings em vez de 
números flutuantes, já que ele faz a conversão.
'''
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
print('---')