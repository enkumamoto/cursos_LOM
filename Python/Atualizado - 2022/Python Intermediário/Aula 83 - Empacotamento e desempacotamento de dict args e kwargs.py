#Empacotamento e desempacotamento de dict
a, b = 1, 2
a, b = b, a
p(a, b)
p('---')

pessoa = {
    'nome': 'Eiji',
    'sobrenome': 'Kumamoto',
}

a, b = pessoa # desta forma desempacota as chaves
p(a, b)
a, b = pessoa.values() # desta forma desempacota os valores
p(a, b)
a, b = pessoa.items() # desta forma desempacota trazendo uma tupla com chave:valor
p(a, b)
(a1, a2), (b1, b2) = pessoa.items() # desempacotamento interno
p(a1, a2)
p(b1, b2)
p('---')

# com laço for
for chave, valor in pessoa.items():
    p(chave, valor)
p('---')

# já temos um dict acima e queremos unir com o dict abaixo
dados_pessoa = {
    'idade': 41,
    'altura': 1.80,
}

p(pessoa, dados_pessoa) #aqui veremos os dois dicionarios juntos, mas não unidos
p('---')
pessoa_completa = {**pessoa, **dados_pessoa} ## assim unirão
p(pessoa_completa)
p('---')

# com laço for
for chave, valor in pessoa_completa.items():
    p(chave, valor)
p('---')

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    p(kwargs)

mostro_argumentos_nomeados(nome='Ananda', idade=37)
p('---')

# laço for dentro da função
def mostro_argumentos_nomeados(*args, **kwargs):
    p('NÃO NOMEADOS:', args)
    for chave, valor in kwargs.items():
        p(chave, valor)

mostro_argumentos_nomeados(41, 1.80, nome='Ananda', idade=37)
p('---')

# aproveitando a função acima para desempacotar os dict unidos
mostro_argumentos_nomeados(**pessoa_completa)
p('---')

