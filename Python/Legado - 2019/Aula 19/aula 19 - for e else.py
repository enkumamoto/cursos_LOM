"""
Uso de lista com for e else
"""
variavel = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junho']

"""
dentro do for pode-se usar continue e break.
comentando somente o continue e o break, deixando o print duplicado, os nomes na lista serão repetidos.
se descomentar somente o break, o laço apresentará o primeiro item da lista e finalizará o programa.
se descomentar somente o continue, o laço irá ignorar o segundo print e fará o ciclo até o último nome 
da lista e finalizará o programa.
"""
for valor in variavel:
    print(valor)
    # continue
    # break
    # print(valor)
print('---')

# o uso do .startswith é para checagem se uma string inicia com uma determinada letra.
variavel2 = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junho']
for valor in variavel2:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
print('---')

'''
Checagem com condicional sem exebir os nomes e convertendo a letra inicial para minúsculo.
Observe o tamanho do código.
'''
variavel3 = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junho']
comeca_com_j = False
for valor in variavel3:
    if valor.lower().startswith('j'):  # o uso do lower() ajuda ao Python na questão de letras maiúsculas ou minúsculas.
        comeca_com_j = True
if comeca_com_j:
    print('Há uma palavra que começa com J.')
else:
    print('Não existe palavra que começa com J')
print('---')

'''
O código acima com uso de else.
Se colocar um continue no lugar do break, ele apresentará todos itens da lista e o else perde a necessidade e ainda
não exibirá palavra com j.
Mas se colocar um pass no lugar do continue, serão exibidos todos os nomes e o else será utilizado.
'''
variavel4 = ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junho']
comeca_com_j = False
for valor in variavel4:
    # print(valor)  # Executando com o print nesta posição, serão apresentados todos as palavras até a palavra com J.
    if valor.lower().startswith('j'):
        # print(valor)  # Executando com o print nesta posição, será apresentado a palavra com J.
        break  # Se o código não achar alguma palavra com J, o break entra em ação e salta para o else.
               # Se caso achar uma palavra com o J o break não saltará ára o else.
        # continue
        # pass
    # print(valor)
else:
    print('Não existe palavra que começa com J')
print('---')
