"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""

# uma das formas mais simples de exemplificar é que se 10 é igual a 10 então varialve será valor:
condicao = 10 == 10
variavel = 'Valor' if condicao else "Outro Valor"
print(variavel)
print('---')

# mas se condicao for falsa será apresentado o valor do else
condicao = 10 == 11
variavel = 'Valor' if condicao else "Outro Valor"
print(variavel)
print('---')

'''quando há validação dos 2 últimos digitos do cpf
podemos usar o código abaixo como exemplo'''
digito = int(input("Digite um número: "))
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
print('---')

# ou 
digito = int(input("Digite um número: "))
novo_digito = 0 if digito > 9 else digito
print(novo_digito)
print('---')