'''
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''
name = 'Eiji'  # uma variável é um apelido para algo salvo na memória
age = 37
height = 1.84
major_age = age > 18  # bool (comparação)
weight = 89

print ('Nome:',name)
print ('Idade:',age)
print ('Altura:',height)
print ('É maior:',major_age)

# A partir do momento que uma ou mais variáveis possuem valores numéricos (int ou float), pode-se realizar operações
# matemáticas com elas.
# print (age * height)
imc = weight/ height ** 2
print (name, 'tem', age, 'e o seu imc é %0.2f'%imc)