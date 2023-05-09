import re
import random

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj): #função que chama funções
    cnpj = remove_caracter(cnpj)
    try:
        if cnpj_seq_numerico(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False
    if novo_cnpj == cnpj:
        return True
    else:
        return False

def remove_caracter(cnpj): #função para retirada de . - e /
    return re.sub(r'[^0-9]', '', cnpj)

def cnpj_seq_numerico(cnpj): #função de checagem de sequencia numerica, pois isso gera cnpj válido
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False

    print(sequencia)

def calcula_digito(cnpj, digito): # função que calcula os digitos do cnpj
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos): # laço for para contagem dos regressivos e soma para validação
        total += int(cnpj[indice]) * regressivo
    digito = 11 - (total % 11)
    digito = digito if digito <=9 else 0

    return f'{novo_cnpj}{digito}'

# a partir daqui são funções para gerar números randomicos para criar CNPJ
def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def gerador():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
        f'{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = calcula_digito(cnpj=inicio_cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    return novo_cnpj

def formata(cnpj):
    cnpj = apenas_numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado