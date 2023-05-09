# Exercício - Sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    p("Pergunta: ", pergunta['Pergunta'])
    p()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        p(f'{i})', opcao)
    p()

    escolha = input("Escolha uma opção: ")
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        p("Acertou!")
    else:
        p("Errou!")

    p()

p(f"Você acertou {qtd_acertos}")
p("de", len(perguntas), "perguntas.")