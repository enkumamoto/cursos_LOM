"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
p('Vamos checar se o número é par ou ímpar!')
number = input('Digite um número inteiro: ')

if number.isdigit():
    number_int = int(number)
    if number_int % 2 == 0:
        p(f'O número {number_int} é par!')
    else:
        p(f'O número {number_int} é ímpar!')
else:
    p('O número digitado não é um número inteiro, por favor use um número inteiro.')
p('---')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora em número inteiros: ")

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        p(f'Bom dia!')
    elif hora_int >=12 and hora_int <=17:
        p('Boa Tarde!')
    elif hora_int >=18 and hora_int <=23:
        p('Boa noite!')
    else:
        p('Não conheço essa hora.')
except:
    p('Por favor, digite só números inteiros.')
p('---')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite o seu primeiro nome: ")

qtd_letras = len(nome)
if qtd_letras <=1:
    p('Seu nome é inválido. digite mais de uma letra.')
elif qtd_letras <= 4:
    p('Seu nome é curto')
elif qtd_letras >= 5 and qtd_letras <= 6:
    p('Seu nome é normal')
else:
    p('Seu nome é muito grande')
p('---')