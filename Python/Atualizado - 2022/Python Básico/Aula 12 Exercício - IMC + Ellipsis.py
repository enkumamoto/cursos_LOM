print("Bem vindo a Calculadora de IMC")
nome = input("Digite seu nome completo: ")
altura = float(input("Digite sua altura em metros (Ex.: 1.75): "))
peso = float(input("Digite o seu peso atual em Kg(Ex.: 56.7): "))

imc = peso / (altura ** 2)

print (f'{nome} sua altura é {altura:,.2f} e seu peso atual é de {peso:,.2f} quilos.')
print (f'O seu IMC é de {imc:,.2f}.')