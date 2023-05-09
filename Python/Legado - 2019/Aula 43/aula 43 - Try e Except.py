# Exceções (Except) são retornos de várias classes, por exemplo, quando uma linha executa algo que retorna erro, esse erro é uma exceção

# o retorno de da linha abaixo é uma exceção gerada pelo python
# print(a)

# mas se usarmos um try o python executará o código mas terá o erro, porém seguido except temos como "mascarar" o erro
try:
    print(a)
except:
    print("Erro")
print("---")

# como dito, o except são retorno de erros de execução do código, pode ser tratado dentro do except (pode ser usado para gerar log)
try:
    print(b) # gera classe de erro NameError
except NameError as erro: # tratando o erro apontando a classe do erro. é a melhor forma de tratar exceção.
    print("Ocorreu um erro, fale como o desenvolvedor.") # Retornará a mensagem e o código continuará rodando

print("Vamos continuar...")
print("---")

# como sabemos que a quantidade de erros são inúmeras pode-se usar a classe Exception e com ela qualquer exceção será direcionada para ela.
# no exemplo abaixo será colocada várias forma de exceções
try:
    a = [] #colocamos "a" como variável para lista
    print(a[1]) #pedido de print de um índice que não existe, mas se tirar o número 1 o código rodará normalmente
except NameError as erro:
    print("Ocorreu um erro, fale com o desenvolvedor.")
except IndexError as erro: # neste ponto o except reconhece que é um erro de índice e retornará a mensagem do print
    print ("Erro de índice.")
except Exception as erro: # neste ponto o except captura qualquer erro que não foi capturado pelos anteriores
    print("Ocorreu um erro inesperado.")
print("Vamos continuar...")
print("---")

# se mudar a variável "a" de lista para dicionário
try:
    a = {} #colocamos "a" como variável para dicionário
    print(a[1]) # aqui gerará um erro de KeyError
except NameError as erro:
    print("Ocorreu um erro, fale com o desenvolvedor.")
except IndexError as erro:
    print ("Erro de índice.")
except Exception as erro: # O erro será capturado aqui
    print("Ocorreu um erro inesperado.")
print("Vamos continuar...")
print("---")

# Então a melhor forma de deixar o código limpo aconselha-se a escreve-lo da forma abaixo
try:
    a = {}
    print(a[1])
except NameError as erro:
    print("Ocorreu um erro, fale com o desenvolvedor.")
except (IndexError, KeyError) as erro: # gerar uma tupla com vários erros e evitar vários except
    print ("Erro de índice ou chaves.")
except Exception as erro:
    print("Ocorreu um erro inesperado.")
print("Vamos continuar...")
print("---")

# Também pode-se usar else dentro do bloco try except
try:
    a = {}
except NameError as erro:
    print("Ocorreu um erro, fale com o desenvolvedor.")
except (IndexError, KeyError) as erro:
    print ("Erro de índice ou chaves.")
except Exception as erro:
    print("Ocorreu um erro inesperado.")
else:
    print("Seu código foi executado com sucesso!")
    print(a)
finally: # a cláusula finally será executada sempre, mesmo com erro acontecendo. é bastanteusada para fechar arquivos dentro do código.
    print("Finalmente.")

print("Vamos continuar...")
print("---")

# pode-se criar blocos try except dentro de outros blocos try except
try:
    a = 0
    try:
        a = 1/0
    except:
        print("Erro.")
except NameError as erro:
    print("Ocorreu um erro, fale com o desenvolvedor.")
except (IndexError, KeyError) as erro:
    print ("Erro de índice ou chaves.")
except Exception as erro:
    print("Ocorreu um erro inesperado.")
else:
    pass
finally:
    a = ""

print(a)