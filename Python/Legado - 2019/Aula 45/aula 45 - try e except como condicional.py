"""Pode-se usar try e except como condicional, os exemplos abaixo mostrarão como fazer isso numa conversão numerica
"""
# Exemplo: para realizarmos uma operação matemática precisamos dizer ao python o que deve ser feito
#numero = input("Digite um número para multiplicar por 5: ")
#print(numero * 5)

# já podemos ver que o código acima repetira qualquer string 5 vezes e o input precisaria receber um int ou um float,
# mas o valor não pode receber os dois ao mesmo tempo e só o float (dependendo da necessidade do código) não servirá.
# para resolver faremos uma função que converte para int e float

def converte_numero(valor):
    try:
        valor = int(valor) # nesta parte da função tentará converter para inteiro
        return valor
    except ValueError: # nesta parte o except passa para uma nova tentativa de converter para float
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
numero = converte_numero(input("Digite um número para multiplicar por 5: "))
if numero is None:
    print("Erro: Isso não é um número.")
else:
    print(numero * 5)
print("---")