import calculos

''' com o import comentado e executando o print, retornará o __main__.
mas se comentar o print e descomentar o import, retornará o nome do módulo.
'''
# print(__name__)

#utilizando o módulo
print(calculos.PI)
print("---")

# utilizano a função multiplica_lista
lista = [2,4,3]
print(calculos.multiplica_lista(lista)) #neste caso estamos usando a lista dentro do aplicativo.py
print("---")

'''Quanto o uso de from módulo import função continua com a mesma lógica'''

from calculos import dobra_lista

lista = [2,4,6,8,10]
print(dobra_lista(lista))
print("---")