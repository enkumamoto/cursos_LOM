"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
def soma(x, y):
    p(x + y)

soma(3,4)
p('---')

# e se usarmos um parâmetro com valor 0? lembre-se que 0 é False então tem que ter cuidado ao usá-lo.
# para evitar problemas faremos uma condicional dentro da função
def soma(x, y, z=0):
    if z:
        p(f'{x=} {y=} {z=}', '|', 'x + y + z= ', x + y + z)
    else:
        p(f'{x=} e {y=}', '|', 'x + y = ', x + y)

soma(3,4) # veja que o print manteve o 0 no z
soma(1,2,3) # veja que o 0 fou trocado por 3 no z
p('---')

# pra ficar mais claro o z precisa ser checado, com isso usaremos 'is' e o ' is not'
def soma(x, y, z=None):
    if z is not None:
        p(f'{x=} {y=} {z=}', '|', 'x + y + z= ', x + y + z)
    else:
        p(f'{x=} e {y=}', '|', 'x + y = ', x + y)

soma(3,4)
soma(1,2,3)
soma(8,9,0) # mesmo que enviem um 0, a função funcionará. observe que se mandado desta forma a função entende que a ordem dos valores é a ordem dos parâmentros.
soma(y=9, z=0, x=8) # já manadado na forma nomeada a função entende que mesmo fora da ordem, cada valor irá para posição correta.
p('---')

'''
todo parâmetro com valor padrão deve ser seguido por um outro parâmetro com valor padrão. caso isso não aconteça, posteriormente, o programa terá um bug
'''
# def soma(x, z=None, y=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', '|', 'x + y + z= ', x + y + z)
#     else:
#         print(f'{x=} e {y=}', '|', 'x + y = ', x + y)

# soma(3,4)
# soma(1,2,3)
# soma(y=9, z=0, x=8)
# print('---')