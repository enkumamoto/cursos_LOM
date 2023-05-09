primeiro_valor = float(input("Digite um valor: "))
segundo_valor = float(input("Digite outro valor: "))

if primeiro_valor == segundo_valor:
    p ("Os valores são iguais.")

elif primeiro_valor > segundo_valor:
    p(f'o número {primeiro_valor} é maior que {segundo_valor}')

elif primeiro_valor < segundo_valor:
    p(f'o número {segundo_valor} é maior que {primeiro_valor}')
