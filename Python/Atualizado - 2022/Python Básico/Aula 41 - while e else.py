"""while / else"""

string = "Valor qualquer"

i = 0 

while i < len(string):
    letra = string[i]

    p(letra)
    i += 1
else:
    p('O else foi executado.')
p('Fora do while.')
p('---')

# se aplicar um break no meio do laço while só o print('Fora do while.') será executado
string = "Valor qualquer"

i = 0 

while i < len(string):
    letra = string[i]

    break

    p(letra)
    i += 1
else:
    p('O else foi executado.')
p('Fora do while.')
p('---')

# uma forma inteligisnte de usar o else com while é achar alguma coisa dentro de uma string ou qualquer outra coisa. abaixo um exemplo para achar o número 5 na string e parar o código quando achá-lo
string = "1 2 3 4 5 6 7 8 9 10"

i = 0 

while i < len(string):
    letra = string[i]

    if letra == "5": # o número 5 não será exibido.
        break

    p(letra)
    i += 1
else:
    p('O else foi executado.')
p('Fora do while.')
p('---')