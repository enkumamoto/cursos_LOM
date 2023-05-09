'''
6 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1
executar duas funções que recebam um número diferente de argumentos.
'''
def mestre(funcao, *args, **kwargs):  # parte da solução para esta função é o uso de *args e **kwargs
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}!'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}!'

executando = mestre(fala_oi, 'Eiji')  # o parâmetro chamado após a função será jogado para o *args e **kwargs na função mestre
executando2 = mestre(saudacao, 'Eiji', saudacao = 'Bom dia')
print(executando)
print(executando2)