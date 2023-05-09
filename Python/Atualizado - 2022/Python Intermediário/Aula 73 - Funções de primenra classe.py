"""
Higher Order Functions
Funções de primeira classe
"""

# abaixo exemplo de função
def saudacao(msg):
    return msg

p(saudacao("Bom dia!"))
p('---')
v = saudacao("Bom dia!")
p(v)
p('---')

# agora uma função que recebe uma função como parâmetro
def saudacao(msg): # 3 - neste momento a função já recebe o dado e envia para a variável 'v'
    return msg

def executa(funcao, texto): # 2 - aqui a função já sabe que deve manter o memory id para que saudacao saiba onde buscar
    return funcao(texto)

v = executa(saudacao, "Bom dia!") # 1 - função executa recebe o "bom dia" para guardar o dado na memória e enviar para função saudacao
p(v) # 4 - imprime o resultado.
p('---')

# refatorando o código para que a saudacao exiba uma saudação com nome
def saudacao(msg, nome):
    return f"{msg}, {nome}!"

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, "Bom dia", "Eiji")
p(v)
p('---')