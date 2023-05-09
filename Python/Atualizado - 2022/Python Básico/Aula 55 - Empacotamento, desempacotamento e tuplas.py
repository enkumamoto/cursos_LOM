"""
Introdução ao empacotamento e desempacotamento + tuplas
"""

'''
o python permite que se faça muitas coisas com os iteráveis
'''
nomes = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior'] # variável com lista como valor
nome1, nome2, nome3, nome4, nome5 = nomes # variáveis recebendo valor por índice no desempacotamento
p(nome1)
p('---')

nome1, nome2, nome3, nome4, nome5 = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
p(nome2)
p('---')

'''
se por acaso há mais valores que variáves, retornará erro: too many values to unpack.
agora, se há mais variáveis que valores, retornará: not enough values to unpack
'''
try:
    nome1, nome2, nome3  = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
    p(nome1)

except ValueError:
    p("Muitos valores para serem desempacotados!")
p('---')

try:
    nome1, nome2, nome3, nome4, nome5, nome6  = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
    p(nome1)

except ValueError:
    p("Não há valores suficientes para serem desempacotados!")
p('---')

'''
digamos que queira somente um valor da lista e queira empacotar todo o resto
'''
nome1, *_  = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior'] # o asterisco diz ao python para pegar os valores não usados e colocar numa outra variável
p(nome1)
p(_)
p('---')

'''
por convenção, devs python usam "*_" para empacotar e ignorar valores numa lista
'''
nome1, *_  = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
p(nome1)
p(_)
p('---')

'''
mas se quiser pegar outro valor deve colocar um "_, variavel, *_" para ignorar os valores anteriores (que não serão empacotados) e empacotar o restante.
'''
_, _, nome, *_  = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior']
p(nome)
p(_)
p('---')