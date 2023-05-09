name = 'Eiji'
age = 37
height = 1.84
major_age = age > 18
weight = 89

imc = weight/ height ** 2
print (name, 'tem', age, 'e o seu imc é %0.2f'%imc)

# para perder menos tempo na digitação de prints com variáveis pode-se usar o fstrigs
# que consiste em colocar a letra 'f' antes das aspas.
print (f'{name} tem {age} e o seu peso é {imc:.2f}')  # Para arredondar o resultado do imc basta colocar um ':.2f'.
                                                      # no caso foram duas casa decimais, mas isso pode variar de
                                                      # acordo com o que é pedido.

# outra formar de realizar o mesmo print acima é usando o 'format()'.
print ('{} tem {} anos e o seu imc é {:.2f}'. format(name, age, imc))  # Lembre-se que o format recebe as variáveis na ordem
                                                                                # que lhe for informada. e o arredondamento é feito dentro
                                                                                # das chaves.

# O format nos permite uma flexibilidade. podemos usar o número da posição da variável (0, 1, 2) dentro das chaves e
# modificar onde entrariam os valores no texto, como também podemos mudar as variáveis
print ('{0} tem {1} anos e o seu imc é {2:.2f}'. format(name, age, imc))
print ('{2} tem {0} anos e o seu imc é {1:.2f}'. format(name, age, imc))
print ('{n} tem {a} anos e o seu imc é {i:.2f}'. format(n=name, a=age, i=imc))
