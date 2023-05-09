# raise - lançando exceções (erros)
# print(123)
# raise ValueError('Deu erro!') # aqui lança um erro criado pelo dev
# print(456)
# ---

# alguns desenvolvedores suprimem os erros, por exemplo:
# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         return n # sumprimindo o erro e retornando o número

# print(divide(8, 1))
# print('---')

# melhorando o tratamentos de erros
# def divide(n, d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentado dividir por zero!') # este if é redundante, mas o raise consegue mudar a mensagem
#     return n / d # este return já traria o ZeroDivisionError, mas em inglês

# print(divide(8, 2))
# print('---')

# lembre-se, trate os erros fora doas funções. 
# uma função tem uma tarefa específica para executar
# então tratamento de erros deve ser feito por 
# outra função ou fora dela
def nao_aceito_zero(d): # checando se o divisor é zero
    if d == 0:
        raise ZeroDivisionError('Você está tentado dividir por zero!')
    return True

def deve_ser_int_ou_float(n): #checando int ou float
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float'
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d
print(divide(8, "0"))
print('---')