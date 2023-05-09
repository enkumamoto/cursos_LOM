'''
Tuplas - Uma lista imutável
'''
nomes = ['Ananda', 'Eiji', 'Duda', 'Nina', 'Junior'] #lista é mutável, ou seja, ela pode ser alterada. já as tuplas não são.
print(nomes)
print(nomes[0])
print('---')

'''
exemplificadno como tuplas são imutáveis
'''
nomes = 'Ananda', 'Eiji', 'Duda', 'Nina', 'Junior' # quando tiramos os colchetes, ou colocando entre parenteses, o python entendo como tupla
print(nomes)
print(nomes[0])

try:
    nomes[1] = "José"
except:
    print('Se o item 1 da tupla permaneceu Eiji, significa que a tupla é imutável.')
    print(nomes)
print('---')

'''
o python permite a conversão de lista para tupla e o inverso.
'''
nomes = tuple(nomes) # convertendo para tupla
print(nomes, type(nomes))
print('---')
nomes = list(nomes)
print(nomes, type(nomes))
print('---')

