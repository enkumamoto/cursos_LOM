"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x e X - Hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a - será abordado mais para frente
"""

# usaremos f-strings a todo momento por ser mais moderno (e mais fácil de ler)
variavel = 'ABC'

print(f'{variavel}') #variáveis em f-stringssempre são colocadas dentro de chaves
print('---')

# se quiser preencher o com caracteres a esquerda ou a direita deve-se colocar ": > ou < qtd de espaços desejados" depois da variável dentro das chaves
print(f'{variavel: >10}') #aqui teremos 7 espaços a esquerda + ABC (3 caracteres) então 10 caracteres (espaço é um caracter)
print(f'{variavel: <10}') #aqui teremos 7 espaços a direita + ABC (3 caracteres) então 10 caracteres (espaço é um caracter)
print(f'{variavel: ^10}') #aqui teremos ABC (3 caracteres) no centro e a divisão inexata dos outros sete espaços e então 10 caracteres (espaço é um caracter)
print('---')

# também pode usar outros caratere, que não espaços, para preencher
print(f'{variavel:@>10}')
print(f'{variavel:!<10}')
print(f'{variavel:?^10}')
print('---')

# manipulação de casa decimais com ":x.f"
print(f'{1000.324586387283429345298:.2f}')

# para exibir hexadecimais
print(f'O hexadecimal de 1500 é {1500:04x}')

# 