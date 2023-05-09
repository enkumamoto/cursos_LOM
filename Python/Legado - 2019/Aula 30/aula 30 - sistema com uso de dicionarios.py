'''
Criando sistema de perguntas e respostas com dicionários
'''
print('Responda as perguntas abaixo.')
questions = {  # Criando dicionarios com perguntas e respostas
    'Pergunta 1': {  # dentro da primeira chave o seu valor é um outros dicionario
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1','b': '4','c': '2',},  # na segunda chave coloca-se outro dicionário com alternativas
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4','b': '10','c': '6',},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1 - 1?',
        'respostas': {'a': '0','b': '1','c': '-1',},
        'resposta_certa': 'a',
    },

    'Pergunta 4': {
        'pergunta': 'Quanto é 80 + 8?',
        'respostas': {'a': '78', 'b': '88', 'c': '68', },
        'resposta_certa': 'b',
    },

    'Pergunta 5': {
        'pergunta': 'Quanto é 500 + 1?',
        'respostas': {'a': '499', 'b': '501', 'c': '500', },
        'resposta_certa': 'b',
    },
}

respostas_certas = 0  # contador de respostas certas

# Primeira iteração
for pk, pv in questions.items():  # acessando as perguntas
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas: ')
# Aqui acessando as respostas
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resp_user = input('Sua resposta: ')

    if resp_user == pv['resposta_certa']: # Aqui checando as respostas
        print ('Acertou miserávi!')
        respostas_certas += 1
    else:
        print('Ixiiiii, você errou!')
    print('\n')

qtd_ques = len(questions)
porcentagem_acerto = respostas_certas / qtd_ques * 100

print (f'Você acertou {respostas_certas} pergunta(s)')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')