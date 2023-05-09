from dados import produtos, pessoas, lista, alunos
from functools import reduce

# A função reduce é uma acumuladora de valores, por exemplo: acumular valores de uma lista
acumula = 0
for item in lista:
    acumula += item #este laço acumulará os valores e depois somá-los

print(acumula)
print("---")

# para usar a função reduce de uma forma coerente segue o exemplo abaixo
soma_lista = reduce(lambda ac, i: i + ac, lista, 0) #esta linha fará uma economia de loops. aqui o "ac" será o acumulador, o "i" de item, a expressão é a soma do número inicial no acumulador,
                                                    # no caso o zero e depois, no loop seguinte, será somado o primeiro número da lista com o número acumulado.

print(soma_lista)
print("---")

# pode-se usar dicionários com a função reduce
soma_precos = reduce(lambda ac, p: p["preco"] + ac, produtos, 0)
print(soma_precos)
print("A média de preços dos produtos é:", soma_precos / len(produtos))
print("---")

soma_idades = reduce(lambda ac, id: id['idade'] + ac, pessoas, 0)
print(soma_idades)
print("A média de idade das pessoas é:", soma_idades / len(pessoas))
print("---")

soma_idades = reduce(lambda ac, id: id['idade'] + ac, alunos, 0)
print(soma_idades)
print("A média de idade dos alunos é:", soma_idades / len(alunos))
print("---")