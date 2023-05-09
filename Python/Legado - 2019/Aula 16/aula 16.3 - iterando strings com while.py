# Será necessário lembrar dos índices. (vide aula 11)
# my_string = 'o rato roeu a roupa do rei de roma.'  # strings são imutáveis.
# c1 = 0
#
# while c < 40:  # está linha irá retornar o erro 'IndexError: string index out of range'
#     print(c, my_string[c])  # durante a contagem de c, seu valor será colocado como referência no índice da string
#     c1 += 1
# print('Fim!')
# print('---')

# a forma abaixo é mais interessante para o contador ser mais preciso
my_string2 = 'o rato roeu a roupa do rei de roma.'
hml_my_string = my_string2.__len__()  # esta variável conta a quantidade de caractéres do valor da string
c2 = 0

while c2 < hml_my_string:  # automaticamente já pega o valor e realiza uma condição para o looping e evitará o erro IndexError: string index out of range
    print(c2, my_string2[c2])
    c2 += 1
print('Fim!')
print('---')

# Como strings são imutáveis, é necessário outra abordagem para manipula-la
my_string3 = 'o rato roeu a roupa do rei de roma.'
hml_my_string2 = my_string3.__len__()

c3 = 0

my_new_string = ''  # está variável sem valor foi adicionada para manipular a str de my_string

while c3 < hml_my_string2:

    if my_string3[c3] == 'r':  # este bloco de código irá pular cada 'r'
#        pass
        my_new_string = my_new_string + my_string3[c3].upper()  # Aqui temos um tratamento para que a letter 'r' fique maiúscula.
    else:
        my_new_string = my_new_string + my_string3[c3]  #

#    print (my_new_string)  # Se essa linha for descomentada, será visto a frase ser montada a cada loop
    c3 += 1
print (my_new_string)
print('Fim!')
print('---')

# Vamos interagir mais com o loop, onde usaremos contadores para interagir com o loop
my_string4 = 'o rato roeu a roupa do rei de roma.'
hml_string = len(my_string4)

c = 0
countering = 0
letter = ''

while c < hml_string:
    cnt = my_string4.count(my_string4[c])

    if countering < cnt and my_string4[c].strip():  # o .strip eliminará os espaços e contará a letra que aprecer mais
        letter = my_string4[c]
        countering = cnt

#    print (my_string4[c], cnt)
    c += 1
print (letter, countering)
print('Fim!')
print('---')

# Caso queira realizar checagem de frases aleatórias com o bloco de código acima:
while True:
    my_string4 = input('Digite uma frase: ')
    hml_string = len(my_string4)

    c = 0
    countering = 0
    letter = ''

    while c < hml_string:
        cnt = my_string4.count(my_string4[c])

        if countering < cnt and my_string4[c].strip():
            letter = my_string4[c]
            countering = cnt

        c += 1
    print (f'Na frase "{my_string4}" a letra "{letter}" aparece {countering} vezes.')
print('Fim!')
print('---')
