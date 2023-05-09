'''
é possível criar, editar, escrever e apagar arquivos com python.
mais detalhes: https://docs.python.org/3/library/functions.html#open
'''

#esta variável criará um arquivo txt em modo escrita e leitura
file = open('abc.txt', 'w+')

#as três linhas abaixo serão escritas no arquivo
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

#neste ponto o arquivo é fechado
file.close()
print('---')

'''
caso queira realizar a leitura após a escrita das linhas no arquivo o código ficará da forma abaixo
'''
file = open('abc1.txt', 'w+')

file.write('Linha 4\n')
file.write('Linha 5\n')
file.write('Linha 6\n')

'''
aqui informamos a posição da leitura ((offset, from_what)
onde f é o ponteiro do arquivo (https://acervolima.com/funcao-python-seek/))

Parâmetros:
Offset: Número de posições para avançar
from_what: Define o ponto de referência.
O ponto de referência é selecionado pelo argumento from_what . Aceita três valores:

    0: define o ponto de referência no início do arquivo
    1: define o ponto de referência na posição atual do arquivo
    2: define o ponto de referência no final do arquivo 
'''
file.seek(0,0)
print("Leitura das linhas:")
print(file.read())
print('####')

'''
uma outra forma de ler as linhas é usaro o readline(), está função faz leitura linha a linha
'''
file.seek(0,0)
print("Leitura das linhas:")
print(file.readline(), end='') #o end= será usado para não ter espaços entre quebras de linha
print(file.readline(), end='')
print(file.readline(), end='') #perceba que esta forma é repetitiva.
print('####')

'''
também pode-se criar listas usando o readlines()
'''
file.seek(0,0)
print("Leitura das linhas:")
print(file.readlines())
print('####')

'''
pode-se usar laço for com readlines()
'''
file.seek(0,0)
for linha in file.readlines(): #também pode-se ler o arquivo diretamente, com isso deve-se retirar o readlines() e manter somente a variável file
    print(linha, end='')

file.close()
print('---')

'''
é possível usar o try e finally dentro da manipulação ou criação de arquivos, porém não é uma boa prática.
'''
try:
    file = open('abc2.txt', 'w+')

    file.write('Linha 7\n')
    file.write('Linha 8\n')
    file.write('Linha 9\n')

    file.seek(0,0)
    print("Leitura das linhas:")
    print(file.read())

finally:
    file.close()
print('---')

'''
a melhor prática em python é usando o gerenciador de contexto, no caso usaremos o with, pois ele, durante a execução do código, abre e fecha o arquivo. 
'''

with open ('abc3.txt', 'w+') as file: #esta linha diz que deve-se abrir o arquivo (com permissão de leitura e escrita) e apontar para variável file
    file.write('Linha 10\n')
    file.write('Linha 11\n')
    file.write('Linha 12\n')

    file.seek(0,0)
    print(file.read())
print('---')

'''
até agora realozou a escrita e a leitura, mas não a edição do arquivo sem compromenter o conteúdo. isso pode ser feito com a função "a" de append
'''
with open ('abc4.txt', 'a+') as file:
    text = input("Digite o novo conteúdo: ")
    file.write(f"{text}\n")
    file.seek(0)
    print(file.read())
print('---')

'''
existe a opção de apagar arquivos usando python, caso o programa tenha essa necessIdade:, basta importar o módulo os
'''
import os

with open ('abc5.txt', 'w+') as file:
    file.write('Linha 13\n')
    file.write('Linha 14\n')
    file.write('Linha 15\n')

    file.seek(0,0)
    print(file.read())

decisao = input("Deseja apagar o arquivo abc5.txt? (S/N): ").lower()

if decisao == "s":
    os.remove('abc5.txt')
    print("Arquivo abc5.txt deletado com sucesso!")
else:
    print("Arquivo abc5.txt não foi deletado!")

print('---')

'''
uma outra coisa que pode ser feita é gerar arquivos json, por exemplo, como dicionário, salvar e acessar
'''
import json

d1 = {
    'Pessoa 1': {
        'Nome:': 'Eiji',
        'Idade:': '40',
    },
    'Pessoa 2': {
        'Nome:': 'Ananda',
        'Idade:': 37,
    },
    'Pessoa 3': {
        'Nome:': 'Duda',
        'Idade:': 11,
    },
    'Pessoa 4': {
        'Nome:': 'Nina',
        'Idade:': '8',
    },
    'Pessoa 5': {
        'Nome:': 'Junior',
        'Idade:': '3',
    },
}

# convertento o dicionário para json

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print('---')