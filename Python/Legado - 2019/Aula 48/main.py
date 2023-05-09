from vendas.calc_preco import aumento,reducao
from vendas.formata import preco

#Calculando preço com aumento de 15%
valor = float(input("Qual o valor do produto: R$"))

reajuste = input("Este valor terá reajuste? (S/N):").lower()

if reajuste == "s":
    opcao = input("É desconto ou acrescimo? (D/A):").lower()
    if opcao == "a":
        up_perc = int(input("Digite qual a porcentagem de acrescimo:"))
        preco_com_aumento = aumento(valor, up_perc)
        print("O valor total é:",preco_com_aumento)

    elif opcao == "d":
        descount = int(input("Digite qual a porcentagem de desconto:"))
        preco_com_desconto = reducao(valor, descount)
        print("O valor total é:",preco_com_desconto)

    else:
        print("Opção inválida.")

else:
    print("Opção inválida.")