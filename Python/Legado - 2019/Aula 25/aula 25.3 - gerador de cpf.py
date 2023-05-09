from random import randint

number = str(randint(100000000, 999999999))

new_cpf = number  # excluindo os dois últimos números.
reverse = 10  # contador reverso para gerar os multiplicadores
total = 0

# Loop do CPF
for index in range(19):  # único loop para criar as 19 voltas
    if index > 8:  # índices de 0 a 9
        index -= 9  # Primeiros 9 números do CPF
    total += int(new_cpf[index]) * reverse  # Total da soma das multiplicações.

    reverse -= 1  # retira um número a cada volta até finalizar no número 2.
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)
        if d > 9:  # Se o dígito for maior que 9 o valor é 0
            d = 0
        total = 0  # zera o total
        new_cpf += str(d)  # concatena 0 dígito gerado no novo cpf

print(new_cpf)
# Evita sequência, Ex.: 11111111111, 00000000000...
# sequency = new_cpf = str(new_cpf[0]) * 11
#
# if cpf == new_cpf and not sequency:
#     print ('Este CPF é válido.')
# else:
#     print ('Este CPF é invalido.')

