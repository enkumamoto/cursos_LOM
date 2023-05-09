import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

# Acima funções para chcagem de números com pontos flutuantes, inteiro, etc.

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# isdigit, isnumeric e isdecimal são módulos built-in para checagem de números.

# isdigit - Retorne true se todos os caracteres da string forem dígitos e houver
# pelo menos um caractere, caso contrário, false. Os dígitos incluem caracteres
# decimais e dígitos que precisam de tratamento especial, como os dígitos sobrescritos
# de compatibilidade. Isso abrange dígitos que não podem ser usados para formar números
# na base 10, como os números de Kharosthi. Formalmente, um dígito é um caractere que
# possui o valor da propriedade Numeric_Type = Digit ou Numeric_Type = Decimal .

# isnumeric - Retorne true se todos os caracteres da string forem caracteres numéricos
# e houver pelo menos um caractere, caso contrário, false. Os caracteres numéricos
# incluem caracteres de dígito e todos os caracteres que possuem a propriedade de valor
# numérico Unicode, por exemplo U + 2155, FRACÇÃO DO VULGAR QUINTA. Formalmente, caracteres
# numéricos são aqueles com o valor da propriedade Numeric_Type = Digit, Numeric_Type = Decimal
# ou Numeric_Type = Numeric .

# isdecimal - Retorne true se todos os caracteres da string forem decimais e houver pelo
# menos um caractere, caso contrário, false. Caracteres decimais são aqueles que podem ser
# usados ​​para formar números na base 10, por exemplo. U + 0660, ZERO DE DÍGITO ÁRBICO-INDIC.
# Formalmente, um caractere decimal é um caractere da categoria geral Unicode “Nd” .

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print ('O resultado é:',num1 + num2)
else:
    print('Número não convertido.')

# Este bloco de código acima apresentará erro ao executar um float, uma maneira de corrigir é usando as funções de checagem
# ou usar o 'try' e 'except'.
# Caso seja digitado qualquer coisa que não seja um número, retornará erro.
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)  # float aceita inteiro e ponto flutuante
    num2 = float(num2)

    print('O resultado é:', num1 + num2)
except:
    print ('Erro.')