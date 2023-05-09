from vendas.formata import preco

def aumento(valor, porcentagem, formata=True):
    r = valor + (valor*(porcentagem/100))
    if formata:
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=True):
    r = valor - (valor*(porcentagem/100))
    if formata:
        return preco.real(r)
    else:
        return r