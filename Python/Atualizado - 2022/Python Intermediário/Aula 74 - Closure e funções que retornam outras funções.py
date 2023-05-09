'''
Closure e funções que retornam outras funções
'''

# geralmente iniciantes pensam que uma função de saudação deve ser assim
def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}!'

s1 = criar_saudacao('Bom dia', 'Nande')
s2 = criar_saudacao('Boa noite', 'Nande')
p(s1)
p(s2)
p('---')

# apresentando o closure.
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar # dessa forma a função apresentará o memory id do dado

s1 = criar_saudacao('Bom dia', 'Nande')
s2 = criar_saudacao('Boa noite', 'Nande')
p(s1()) # quando acrescentado os parenteses após a variável, o python entende que a função saudar no return está completa
p(s2) # sem closure para apresentar o memory id
p('---')

# usando o closure e usando outras possibilidades
def criar_saudacao(saudacao):
    def saudar(nome): # transferindo nome para saudar para ficar mais dinâmico
        return f'{saudacao}, {nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

p(falar_bomdia("Eiji")) # passando o nome dentro do closure
p(falar_boanoite("Nande"))
p('---')

# usando um laço for com lista de nomes
def criar_saudacao(saudacao):
    def saudar(nome): # transferindo nome para saudar para ficar mais dinâmico
        return f'{saudacao}, {nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['Ananda', 'Duda', 'Eiji', 'Nina', 'Junior']:
    p(falar_bomdia(nome))
    p(falar_boanoite(nome))
p('---')