'''
Um função decoradora é uma função (ou outro objeto chamável) que recebe uma função como parâmetro e retorna uma função.
Essa nova função que é retornada pelo decorador é que fica associada ao nome da função original.

Para entendermos melhor o conceito, vamos começar com uma função básica que fala oi.
'''

def fala_oi():
    print('Oi!')

fala_oi()
print('---')

# agora vamos chamar a função a partir de uma variável.
variavel = fala_oi

variavel()
print('---')

# se quiser checar o tipo de variavel
print(type(variavel))
print('---')

# o python permite criar funções dentro da função
def main(): #esta parte da função cria a segunda função.
    def second():
        print('Oi!')
main() # se executarmos da forma que está, o retorno é inexistente
print('---')

# para que a função acima funcione, deve-se escrevê-la da forma abaixo
def main():
    def second():
        print ("Oi!")
    second() # neste caso, estamos executando a função dentro dela ou usar o return
main()
print('---')

# uma forma de usar uma função que não faz parte da anterior mas imprimir seu resultado.
def main(funcao): #aqui o main recebe uma função qualquer como parametro
    def second(): #esta segunda função está fazendo o trabalho executar a função que a master está recebendo como parametro
        funcao()
    return second

def fala_tra():
    print("Tra!")

variavel = main(fala_tra)
variavel()
print('---')

#Para confirmar que a função é decorada, escreveremos um código confirmando
def main(funcao):
    def second():
        print("Agora estou decorada!") #adicionamos está frase para confirmar
        funcao()
    return second

def fala_tra():
    print("Tra!")

fala_tra = main(fala_tra)
fala_tra()
print('---')

# usando decorador
def main(funcao):
    def second():
        print("Agora estou decorada!") #adicionamos está frase para confirmar
        funcao()
    return second

@main #decorador
def fala_tra():
    print("Tra!")

# fala_tra = main(fala_tra) # esta linha foi comentada por não ter utlidade já que usamos um decorador.
fala_tra()
print('---')

# e se caso quisermos que várias funções passem pelo main? deverá usar args e kwargs
def main(funcao):
    def second(*args, **kwargs):
        print("Agora estou decorada!") #adicionamos está frase para confirmar
        funcao(*args, **kwargs)
    return second

@main #decorador
def fala_tra():
    print("Tra!")

@main
def outra_funcao(msg): #o msg receberá o valor "Olá, eu sou Eiji!"
    print (msg)

outra_funcao("Olá, eu sou Eiji!")

fala_tra()
print('---')

