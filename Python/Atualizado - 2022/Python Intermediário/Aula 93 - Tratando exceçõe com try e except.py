# try, except, else e finally

'''
o python, em seu manifesto, fala que nenhum erro deve passar silenciosamente
a não ser que sejam explicitamente silenciados.
com isso mostrar um erro tratado
'''
a = 18
b = 0
# c = a /b # esta variável descomentada retornará o ZeroDivisionError, 
# mas se comentar a variável c ou mudando o valor de b o print funcionará

try:
    ...

except:
    ...

print("Continua")
print('---')

# tratando o erro
a = 18
b = 0

try:
    c = a / b # python tenta executar

except:
    ...

print("Continua")
print('---')

# mesmo que coloque as variáveis dentro do try, o python tratará o erro
try:
    a = 18
    b = 0
    print('linha 1') #demonstrando que o python executou o código
    c = a / b # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except:
    print('Except executado')

print("Continua")
print('---')

# veja que tratar erros desta forma, 
# gera problema, por que não saberá 
# qual erro aconteceu.
# com isso seguindo o formato do 
# exemplo, trataremos o erro ZeroDivisionError
try:
    a = 18
    d = 0
    print('linha 1') #demonstrando que o python executou o código
    c = a / d # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except ZeroDivisionError: # informando a classe do erro
    print('Except executado')

print("Continua")
print('---')

# mas se não fosse esse erro e sim outro?
try:
    a = 18
    # f = 0 # gerando um NameError: name is not defined
    print('linha 1') #demonstrando que o python executou o código
    c = a / f # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except ZeroDivisionError: # informando a classe do erro
    print('Except executado')

except NameError:
    print('f não está definido')

print("Continua")
print('---')

# outros tratamentos
try:
    a = 18
    g = 0 # gerando um NameError: name is not defined
    print(g[0])
    print('linha 1') #demonstrando que o python executou a linha anterior, houve erro e salta para o último except
    c = a / g # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except ZeroDivisionError: # informando a classe do erro
    print('Except executado')

except NameError:
    print('f não está definido')

except Exception:
    print('ERRO DESCONHECIDO')

print("Continua")
print('---')

# pode-se tratar erro numa mesma linha de except e exibindo o erro
try:
    a = 18
    h = 0 # gerando um NameError: name is not defined
    print('linha 1'[1000]) #gerando erro para a tupla (TypeError, IndexError)
    c = a / g # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except ZeroDivisionError: # informando a classe do erro
    print('Except executado')

except NameError:
    print('f não está definido')

except (TypeError, IndexError) as error: # criando alias
    print('TypeError + IndexError')
    print(f'O erro encontrado: {error}')
    print(f'Nome do erro: {error.__class__.__name__}')

except Exception:
    print('ERRO DESCONHECIDO')

print("Continua")
print('---')

#agora tratando o erro de divisão por zero
try:
    a = 18
    b = 0
    print('linha 1') #demonstrando que o python executou o código
    c = a / b # python tenta executar
    print('linha 2') #demonstrando que o python executou a linha anterior, houve erro e salta para o except

except (ZeroDivisionError) as error:
    print('Ococrreu um erro!')
    print(f'O erro encontrado: {error}')
    print(f'Nome do erro: {error.__class__.__name__}')


print("Continua")
print('---')