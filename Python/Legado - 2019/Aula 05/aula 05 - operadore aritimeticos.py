# O operadores aritiméticos em python são
'''
+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
** exponenciação
% resto da divisão (ele retorna um módulo, o resto da divisão entre dois números)
()
'''

print ('Multiplicação 10 * 10 =',10 * 10)
print ('Adição 10 + 10=',10 + 10)
print ('Subtração 10 - 5=',10 -5)
print ('Divisão 10 / 2=', 10 / 2)

# Fique atento que o '*' também serve como multiplicador de string
print (10 * 'Eiji')

# Já o sinal de '+' realiza concatenação de strings, e se tentar somar um número a uma string o python retorna erro.
print (5 + 5)  # Aqui rolará uma soma
print ('5' + '5')  # Aqui rolará uma concatenação
print ('Eiji'+' '+'Kumamoto')  # Concatenação de strings
print ('Eiji'+' '+'Kumamoto e ele tem ' + str(37) + ' anos')  # Concatenação de strings e conversão de int para str, mas
                                                              # não é a melhor forma de escrever o código.
# quando realiza-se divisões dentro do python duas coisas ocorrem, a primeira é que se realizarmos uma divisão com uma
# '/', pode gerar resultado com ponto flutuante e a segunda é que usando '//' o valor será arredondado independende do
# resultado gerado.
print (10 / 3.2)
print (10 // 3.2)

# usando o '%' ele apresentará o resto da divisão
print (10 % 5)  # retornará 0
print (10 % 3)  # retornará 1

# o uso dos parenteses é igual na matemática
print (5+2*10)  # aqui será multiplicado 5 e 10 e depois somado com 5 que dará 25
print ((2+5)*10)  # a lógica matemática diz que quando houver operação entre parenteses,
                  # ela deve ser resolvida primeiro e depois passar para próxima.
