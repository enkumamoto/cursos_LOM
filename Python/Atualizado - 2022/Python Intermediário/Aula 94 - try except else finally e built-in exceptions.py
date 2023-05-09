# um bloco try nunca por aparecer sozinho
#  sempre deve ter um acompanhamento
try:
    print(1)

finally: # o finally sempre será executado mesmo que aconteça um erro.
    print(2)
print('---')

# exemplo do finally com mais detalhes

try:
    print("ABRIR ARQUIVO")
    8/1

finally:
    print("FECHAR ARQUIVO")
print('---')

# o except pode vir no corpo de código junto com o finally
try:
    print("ABRIR ARQUIVO")
    9/0
except ZeroDivisionError:
    print('Dividiu zero')
finally:
    print("FECHAR ARQUIVO")
print('---')

# usando o else
try:
    print("ABRIR ARQUIVO")
    # 9/0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print("FECHAR ARQUIVO")
print('---')