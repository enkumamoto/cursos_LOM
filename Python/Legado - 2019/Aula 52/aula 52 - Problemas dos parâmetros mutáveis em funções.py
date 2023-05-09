'''
nesta parte falaremos sobre argumentos mutáveis em funções
'''

def lista_de_clientes(clientes_iteravel, lista=[]): # está função unirá duas listas
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)
print("---")
# mesmo que se adicione mais uma lista de cliente distintos e mantendo os mesmo print, seus nomes serão acrescentados.

def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(["José"])

print(clientes1)
print(clientes2)
print("---")

# para solucionar, e para que todas as listas fiquem independentes, vamos modificar o código da seguinte forma

def lista_de_clientes(clientes_iteravel, lista=None): #a primeira coisa é atribuir o valor da lista com None
    if lista is None: #quando o if confirma o none ele cria uma nova lista
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(["José"])

print(clientes1)
print(clientes2)
print(clientes3)
print("---")