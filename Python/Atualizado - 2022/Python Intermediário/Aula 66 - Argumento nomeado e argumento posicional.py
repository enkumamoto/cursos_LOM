"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
# exemplo de função com argumento posicional
def soma(x, y): # significa que cada argumento receberá o valor de acordo com a sua posição
    p(x + y)

soma(3,4)
p('---')

# deixando mais claro
def divide(x, y):
    p(x / y)

divide(10, 2) # note que os resultados serão diferentes
divide(2, 10)
p('---')

# uma outra forma de escrever
def soma(x, y): 
    p(f'{x=} e {y=}', '|', 'x + y = ', x + y)

soma(3,4)
#ou
soma(y=10, x=5)
p('---')

# sempre ter atenção com a quantidade de parâmetros declarados, 
# essa quantidade posicional pode gerar erros pela falta. 

def soma(x, y, z): # se declarado 3 argumentos
    p(f'{x=} {y=} {z=}', '|', 'x + y + z= ', x + y + z)

soma(3, 4, 10) # e aqui também deve-se declarar o valor para o terceiro argumento
# ou
soma(3, 9, z=6) # não é muito recomendado misturar argumentos nomeados com não nomeado.
p('---')

