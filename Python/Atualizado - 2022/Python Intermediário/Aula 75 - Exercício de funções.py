# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

while True:
    algarismo = int(input("Digite um número: "))

    operacao = input("Escolha (2) para duplicar, (3) para triplicar ou (4) quadruplicar o número digitado: ")

    if operacao == "2":
        duplicar = criar_multiplicador(2)
        p(f"Você duplicou {algarismo} e o resultado é {duplicar(algarismo)}!")

    elif operacao == "3":
        triplicar = criar_multiplicador(3)
        p(f"Você triplicou {algarismo} e o resultado é {triplicar(algarismo)}!")

    elif operacao == "4":
        quadruplicar = criar_multiplicador(4)
        p(f"Você duplicou {algarismo} e o resultado é {quadruplicar(algarismo)}!")

    else:
        p("Opção inválida!")
        break