"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1 # aqui temos uma variável global do módulo

def escopo(): # cada função é como um mundo próprio e que nada afeta
    x = 10 # esta variǘel é local, ou seja, por mais que a global tenha o mesmo nome a local não será afetada

    def outra_funcao():
        x = 11
        y = 2
        p(x, y) # imprime o x e y local
    outra_funcao()

    p(x) # imprime o x local dentro da função escopo

p(x) # imprime o x da funçao escopo
escopo()
p(x) # imprime o x (global) do módulo
p('---')

'''
agora, se caso queira que o x global seja impresso dentro das funções deve-se utilizar
'''
x = 1 # aqui temos uma variável global do módulo

def escopo():
    global x # se colocado global dentro do escopo
    x = 10

    def outra_funcao():
        #global x # esse aqui se descomentado passa a ser o x global
        x = 11
        y = 2 
        p(x, y)
    outra_funcao()
    p(x)

p(x)
escopo()
p(x)
p('---')