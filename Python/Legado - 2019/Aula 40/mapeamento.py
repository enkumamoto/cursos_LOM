'''
para usar os dados do arquivo dados.py usaremos o from apontado para dados e importaremos as
variáveis do arquivo. lembre-se que todos os arquivos devem estar na mesma pasta
'''
from dados import produtos, pessoas, lista

# com o mapeamento pode-se realizar diversas tarefas, como por exemplo multiplicar itens de uma lista.
# a função map recebe uma função como primeiro argumento, por isso o uso do lambda, o x é uma variável
# para receber cada item da lista e por fim o multiplicar cada item por 2.
# a função map não retornará uma lista mas sim um iterador.
nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x * 2 for x in lista]   # se tem uma boa noção de list comprehension não há necessidade do map

print (lista)
print (list(nova_lista))  # para o iterador funcionar normalmente, converte-se para lista. type casting
print('---')

'''A função map trabalha melhor com dicionários, no exeplo abaixo usaremos um laço for. porém abaixo
   será apresentado o dicionário completo sem o uso do map.
'''
for produto in produtos:
    print(produto)
print('---')

'''
no exemplo abaixo aprofunda-se o uso do map para pegar somente os preços dos produtos e acrescentar 5% ao valor
original. mas começaremos criando um dicionário só com preços dos produtos.
'''
precos = map (lambda p: p ['preco'], produtos) # o primeiro 'p' é para produtos para retorna o valor da chave preco vindo do dicionário produtos para compor o novo dicionário p

for preco in precos:
    print(preco)
print('---')

# agora aumentando o valor do preço dos produtos sem modificar a estrutura do dicionário
def aumenta_preco(p):
    p['preco'] = round(p['preco'] *1.05, 2) # aqui a função pegará o preço, aumentará em 5% (*1.05) e deixará com duas casa decimais
    return p # retornará o dicionaário sem modificar a estrutura mas com o preço dos produtos aumentado

novosprodutos = map(aumenta_preco, produtos) # a função map mapeia uma função que passa em cada elemento iterável.

for produto in novosprodutos:
    print(produto)
print('---')

# usando dicionário com nome de pessoas
nomes = map (lambda p: p ['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
print('---')

# mesma coisa para idades e a lógica para aumentar a idade segue a mesma dos preços dito acima


def aumenta_idade(p):
    p['nava_idade'] = round(p['idade'] *1.20) # aqui a função criará uma nova chave e valor com uma idade acrescida de 20% da idade otiginal
    return p

nomes = map (aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
print('---')