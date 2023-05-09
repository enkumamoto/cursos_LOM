# https://docs.python.org/3/library/exceptions.html nesta página encontrará lista de exceptions

# Sabemos que números divididos por zero terá resultado zero e essa operação traz erro para o python, com isso
# iremos printar o erro de outra forma
def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error: # tratamento do erro dentro da função, mas modificando o comportamento do python
        print(error)
        return False
print(divide(2,0))
print("---")

# Dessa forma há como ter logs do que ocorre na execução e também ajudar outros desenvolvedores a entender
# os erros que acontecem dentro do código. no exemplo abaixo teremos uma forma de relançar o erro
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print("Log:", error) # nesta parte do código será relançada o erro mas com formato de "log"
        raise

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error) #aqui temos a captura e o retorno do erro
print("---")

# caso queira levantar a própria exceção veja o exemplo abaixo
def divide (n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.") # aqui foi definida uma mensagem para que retorne uma msg não técnica.
    return n1 / n2
try:
    print(divide(n1=2,n2=0))
except ValueError as error: # mudando comportamento do python para exibir a msg não técnica
    print("Você está tentando dividir por 0.")
    print("Log:", error)
print("---")