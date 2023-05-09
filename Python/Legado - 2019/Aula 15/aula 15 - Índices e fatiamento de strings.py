'''
Manipulação de strings
* String índices
* Fatiamento de strings [início:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''
# positivos  [012345678] <------ índice do valor da variável.
text = 'Python s2'  # não fazer isso, é feio

print (text[2])  # aqui será apresentado só a letra 't' já que ele está no índice 2
print (text[8])
print ('---')

# negativos -[987654321]
url = 'www.eijikumamoto.com/'
print (url[:-1])  # neste caso aqui será apresentado a url sem a barra
print ('---')

# Caso queira pegar parte de uma string de alguma variável, pode-se delimitar o range que quer buscar.
sub_text = text [2:6]  # Aqui diz: apresentar somente o valor de text do índice 2 até o 6.
sub_text2 = text [:6]  # Aqui diz: apresentar somente o valor de text do início do índice até o 6.
sub_text3 = text [7:]  # Aqui diz: apresentar somente o valor de text do índice 7 até o final.
sub_text4 = text [-9]  # Aqui diz: apresentar somente o valor de text na posição -9.
sub_text5 = text [-9:-4]  # Aqui diz: apresentar somente o valor de text do índice -9 até o -4.
sub_text6 = text [0::2]  # Aqui diz: apresentar o valor de texte pulando de 2 em 2 dentro do índice desde seu início.
print (sub_text)
print (sub_text2)
print (sub_text3)
print (sub_text4)
print (sub_text5)
print (sub_text6)
print ('---')
# Caso queria verificar a quantidade de carateres no valor da variável
print (len(text))
print ('---')
for letra in text:  # aqui mostra uma manipulação do valor.
    print (letra)
print ('---')