# Meta caracter
# ^ ---> comeca com
# $ --->
import re 

#testando com cpf e validacao
cpf = 'a 934.675.235-13' # simulando um erro de digitacao mas capturando o cpf
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print("---")

cpf = '934.675.235-13    aaaaaa'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
print('---')

cpf = '934.675.235-13    aaaaaa'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf)) # aqui retorno sera vazio porque tem letras ao final
print('---')

# exemplificando o uso de negacao de range de letra e capturar so o cpf
cpf = 'akhcbahkf 934.675.235-13 aaaaaa'
print(re.findall(r'[^a-zA-Z ]+',cpf)) # negando letras espacos
print('---')