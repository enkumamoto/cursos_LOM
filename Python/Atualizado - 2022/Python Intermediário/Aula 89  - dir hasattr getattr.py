# dir, hasattr e getattr
string = "Eiji"

#hasattr checa se há um nome dentro do objeto
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper)
    print('---')

print(string)
print('---')

'''
se tentar declarar um método numa variável restornará erro
string = "Eiji"
metoro = 'upper' # por que é uma string
if hasattr(string, metodo):
    print('Existe upper')
    print(string.metodo()) #o erro é que o python tentará usar o método metodo(), que não existe
    print('---')

print(string)
print('---')
'''

# porém o getattr resolve o problema, mas é melhor sempre usar os métodos do python

string = "Eiji"
metodo = input('Digite o método a ser usado: ') # por que é uma string
if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)()) # desta forma o getattr executa o valor da variável como método
    print('---')
# caso o método não exista
else:
    print(f'Não existe o método {metodo}')
print(string)
print('---')