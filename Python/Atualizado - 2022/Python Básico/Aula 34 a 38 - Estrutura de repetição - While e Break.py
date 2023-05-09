
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

# Acima é um loop infinito, mas para para o loop use o break
    if nome == 'sair':
        break
print("Acabou!")
print('---')

# o while é para enquanto for verdadeiro e quando for falso ele deve parar, abaixo um exemplo disso usando um contador
contador = 0

while contador <= 10:
    print(f'Contando {contador}')
    contador = contador + 1
    
print('Acabou!')
print('---')

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 0

while contador <= 10:
    print(f'Contando {contador}')
    contador += 1
    
print('Acabou!')
print('---')

'''
além da palavra break também temos a continue. o continue serve para que o loop reinicie sem passar por uma parte do bloco de código.
no exemplo abaixo, o contador contará até 100, saltará o número 6 e realizará o break no número 40.
'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Saltou, não vou mostrar o 6!')
        continue

    elif contador == 40:
        print('Parou no 40!')
        break
    
    print(f'Contando {contador}')

print('Acabou!')
print('---')

'''
While + while, sim é possível ter while dentro de while. no caso abaixo será apresentado somente a quantidade de linhas e não de colunas
'''
qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    print(linha)
    linha += 1

print('Acabou!')
print('---')

'''
para apresentar as colunhas seguiremos como abaixo
'''
qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
        
    linha += 1

print('Acabou!')
print('---')