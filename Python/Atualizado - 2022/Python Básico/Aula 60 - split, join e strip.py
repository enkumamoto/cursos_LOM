"""
split e join com list e str
split - divide uma string (retorna uma lista)
join - une uma string
"""
frase = "Olha só que, coisa interessante"
# texto = open('/home/eiji/Documentos/texto_teste.txt')
#print(f.read())

# demonstrando o split
lista_palavras = frase.split() # o split sem argumento separará as palavras de acordo com os caracteres brancos e assim gerando uma lista de palavras
# conteudo = texto.read()
# lista_texto = conteudo.split()
print(lista_palavras)
# print(lista_texto)
print('---')

# caso queira definir o separador do split, deve-se especificar quem será o separador
lista_palavras = frase.split(',') # aqui mostramos que a vírgula será o separador
print(lista_palavras) # e assim criaremos uma lista de frases.
print('---')

# usando o for
for i, frase in enumerate(lista_palavras):
    print (lista_palavras[i].strip()) # o strip corta os espaços em branco dentro da string
print('---')

# caso o texto venha com problemas de espaçamento
frase = "     Olha só que                         ,     coisa interessante                          "
lista_palavras = frase.split(',')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = (lista_palavras[i].strip())
    print (lista_palavras[i].strip())
print(lista_palavras)
print('---')

# não é uma boa prática manipular índices diretamente na lista, deves sempre apontar os resultados para uma nova lista
frase = "     Olha só que                         ,     coisa interessante                          "
lista_palavras_cruas = frase.split(',')
lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())
    print (lista_palavras[i].strip())
print(lista_palavras_cruas)
print(lista_palavras)
print('---')

#demonstrando join
frase = "     Olha só,     que coisa interessante                          "
lista_palavras_cruas = frase.split(',')
lista_palavras = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_palavras.append(lista_palavras_cruas[i].strip())

frase_unidas = ",".join(lista_palavras)
print(frase_unidas)
print('---')