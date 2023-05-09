'''
Flags (Bandeiras) - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
'''

v1 = 'a'
v2 = 'b'

print(id(v1))
print(id(v2))
print('---')

# as vezes precisamos saber por onde o interpretador passou, seja por qualquer motivo. e isso depende do algoritimo que está sendo criado.

# abaixo um exemplo com condição falsa.

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo.')
else:
    print('Não faça algo.')

print(passou_no_if, passou_no_if is None) # este print nos mostra que condicao é falsa está passando no if, mas mostra que a variável continua sendo None.
print(passou_no_if, passou_no_if is not None) # este print nos mostra que a variável dentro do if é falsa.
print('---')

# abaixo um exemplo com condição verdadeira.

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo.')
else:
    print('Não faça algo.')

print(passou_no_if, passou_no_if is None) # este print nos mostra que condicao é verdadeira está passando no if, mas mostra que a variável muda de None para True.
print(passou_no_if, passou_no_if is not None) # este print nos mostra que a variável dentro do if é verdadeira.
print('---')

# se ainda assim quiser realizar uma chcagem de passagem pelo if para saber se a condição é verdadeira ou falsa, veja o exemplo abaixo

condicao = True
#condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo.')
else:
    print('Não faça algo.')

if passou_no_if is None: # se o valor de condicao for False será mostrado este print.
    print('Não passou no if.')

if passou_no_if is not None: # se o valor de condicao for True será mostrado este print. ou pode usar somente o else.
    print('Passou no if.')
print('---')

