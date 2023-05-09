'''
Formatando valores com modificadores.
Será usado comando format e o fstrings

:s - Texto (String (str))
:d - Inteiros (int)
:f - Números com ponto flutuante (float)
:.(número)f - Quantidade de casa decimais (float)
:(caractere)(> ou < ou ^)(quantidade)/(tipo - s, d ou f)
> - Esqueda
< - Direita
^ - Centro
'''
num1 = 1
num2 = 3
divisao = num1 / num2
print (divisao)
print ('---')

# aqui retornará um resultado de dízima. abaixo um exemplo de formatação usando "'{:.xf}'.format()".
# obs.: o 'x' representa quantas casa decimais devem ser apresentadas.
print ('{:.2f}'.format(divisao))
print ('---')

# também pode-se usar o fstrings
print (f'{divisao:.2f}')
print ('---')

# Caso queira formatar uma string deve-se usar o :s
nome = 'Eiji Kumamoto'
print (f'Nome: {nome:s}')
print ('---')

# Pode-se completar as as strings com algo que queira, por exemplo, com zeros
num3 = 1
num4 = 1150
print (f'{num3:0>10}')  # neste caso será preenchido com 9 zeros a esquerda e teremos uma limitação de 10 casas.
print (f'{num4:0>10}')
print ('---')

# Pode-se apresentar um número inteiro como float sem converte-lo
num5 = 1
num6 = 1150
print (f'{num5:.2f}')  # adicionando duas casas decimáis
print (f'{num6:.2f}')
print ('---')

# Também pode interagir varias formatações
num5 = 1
num6 = 1150
print (f'{num5:0>10.2f}')  # adicionando duas casas decimais e zeros a esqueda, o ponto flutuante entra na contagem das 10 casas.
print (f'{num6:0>10.2f}')
print ('---')

# Também funciona com palavras
user = 'Eiji Kumamoto'
print (user.__len__())
print(f'{nome:#^21}')
print ('---')

# Usando a função format
name = 'Eiji Kumamoto'
formated_name = '{:@>20}'.format(name)  # as chaves servem para usar os formatadores
print (formated_name)
print ('---')

# Acessando como índice
fname = 'Eiji'
sname = 'Kumamoto'
flname = '{1}'.format(fname, sname)
print (flname)
print ('---')

# outros módulos de formatação
mname = 'Eiji kumamoto NeTo'
print (mname)
print (mname.lower())
print (mname.upper())
print (mname.title())
