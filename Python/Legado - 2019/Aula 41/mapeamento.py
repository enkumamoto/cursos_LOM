'''
para usar os dados do arquivo dados.py usaremos o from apontado para dados e importaremos as
variáveis do arquivo. lembre-se que todos os arquivos devem estar na mesma pasta
'''
from dados import produtos, pessoas, lista

# A linha abaixo criará uma nova lista com números acima de 5 retornará como true
nova_lista = filter(lambda x: x > 5, lista)
print (list(nova_lista))

# também é possível realiza um list comprehension com 'for'
nova_lista = [x for x in lista if x > 5]
print (list(nova_lista))

# agora filtrando produtos e criando dicionário
nova_lista = filter(lambda p: p['preco'] > 50, produtos)

# criaremos um laço for para ver melhor os dados
for produto in nova_lista:
    print(produto)
