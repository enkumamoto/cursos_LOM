# str - strings: é um dado primitivo em python, tudo em python em é um objeto. Strings são textos dentro de aspas.

# O código abaixo está errado porque o texto não está entre aspas, o interpretador do python
# irá procurar como comando e retornará um erro.
# print (alguma coisa)
# Para que ele tenha a saída correta deve-se seguir da forma apresentada abaixo:
print ('alguma coisa')
print ("Aspas duplas")

# Python é uma liguagem de tipagem dinâmica
print (123456)  # O python reconhece que pode imprimir números inteiros
print ('123456')  # Como pode também imprimir números com strings
# print ('Esta linha é uma 'string' (str).')  # Esta linha de código está incorreta, já que o python interpreta a
                                            # tudo de cima para baixo e da esquerda para direita. Neste caso a
                                            # palavra string entre aspas simples declara um comando e isso trará
                                            # erro, já que string não é comando. Existem várias formas de corrigir
                                            # o erro, pode-se usar FSTRING, ou FORMAT ou simplesmente acrescentar as
                                            # aspas duplas como mostrado abaixo.
print ("Esta linha é uma 'string' (str).")

# Também pode-se usar caracter de escape, porém deixará o código "feio".
print ("Esse é o meu \"texto\" (str).")

# Também cuidado com o '\n' pois ele quebra a linha do código, então para exibi-lo o código fica assim:
print (r'Esse é o meu \n (str).')   # Como pode ver, foi usado um 'r' antes das aspas, o interpretador do
                                    # python entende que deve ignorar (não executar) os comandos dentro do print.
                                    # Então fique atento como e quando usar o 'r'.

