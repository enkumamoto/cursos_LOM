'''
CPF = 168.995.350-09
-------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  # 11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          # Digito 2 = 9
'''
while True:
    cpf = input('Digite um CPF: ')
    # cpf = '16899535009'
    new_cpf = cpf[:-2]  # excluindo os dois últimos números.
    reverse = 10  # contador reverso para gerar os multiplicadores
    total = 0

    for index in range(19):  # único loop para criar as 19 voltas
        if index > 8:  # índices de 0 a 9
            index -= 9  # Primeiros 9 números do CPF
        total += int(new_cpf[index]) * reverse  # Total da soma das multiplicações.

        reverse -= 1  # retira um número a cada volta até finalizar no número 2.
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)
    if cpf == new_cpf:
        print ('Válido')
    else:
        print ('Invalido')
        break
