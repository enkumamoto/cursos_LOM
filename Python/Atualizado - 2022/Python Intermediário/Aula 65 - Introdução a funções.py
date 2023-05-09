"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
#Exemplo de função
def Print():
    p("Várias")
    p("Várias")
    p("Várias")
Print()    
p('---')

# também pode criar funções com obrigatoriedade de argumentos (parâmetros)
def imprimir(a, b , c):
    p(a, b, c)
imprimir(1, 2, 3)
imprimir(4, 5, 6)
p('---')

# entenda que passar uma parâmetro numa função é para exemplificar, 
# futuramente usaremos fuções de modo diferentes
def saudacao(nome):
    p(f"Olá, {nome}!")

saudacao('Ananda')
saudacao('Duda')
saudacao('Eiji')
saudacao('Nina')
saudacao('Jujunho')
p('---')

# em caso da função não receber um parâmetro basta deixar a variável com valor
def saudacao(nome='Sem nome!'):
    p(f'Olá, {nome}!')

saudacao('Ananda')
saudacao('Duda')
saudacao('Eiji')
saudacao('Nina')
saudacao('Jujunho')
saudacao() # assim a função receberá o valor da variável.
p('---')