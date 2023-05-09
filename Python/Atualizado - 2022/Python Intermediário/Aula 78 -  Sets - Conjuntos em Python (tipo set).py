'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}
Atenção: sets se apresentam como dicionários, mas só com VALOR e não com chave:valor
'''
s1 = set() # pode-se criar com a classe set
p(s1)
p('---')
s1 = set('Eiji')
p(s1, type(s1)) # perceba que a sequência de letras não é ordenada e que letras repetidas só aparece uma vez.
p('---')
s1 = {'Eiji', 1, 4, "Nande"}
p(s1, type(s1))
p('---')

'''
Sets são eficientes para remover valores duplicados
de iteráveis.
- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos;
- não tem índeces;
- não garantem ordem;
- são iteráveis (for, in, not in)
'''
s1 = {1,2,3,3,3,3,4,5,6,7,5,4,3,4,5,6,7,8,9}
p(s1)
p('---')

#convertendo lista (método longo)
l1 = [1,2,3,3,3,3,4,5,6,7,5,4,3,4,5,6,7,8,9]
s1 = set(l1)
l2 = list(s1)
p(l2, type(l2))
p('---')

# usando set para trabalhar em pesquisa
s1 = {1,2,3,3,3,3,4,5,6,7,5,4,3,4,5,6,7,8,9}
p(4 in s1) #retorna um booleano
p(11 in s1) #not in também funciona
p('---')

# com laço for
for numero in s1:
    p(numero)
p('---')

# Métodos úteis:
# add, update, clear, discard
#usando o add
s1 = set()
s1.add('Eiji')
# s1.add(1,2,3) # o add so aceita um item por vez
s1.add(1)
p(s1)
p('---')

# usando update
s1.update('Nande') #desta forma cada letra será um valor
p(s1)
s1.update(('Nande', 1, 2, 3, 4)) # passando uma tupla, o Nande virá como palavra e o 1 não repetirá
p(s1)
p('---')

# quando o discard é usado é preciso passar o valor a ser descartado
s1.discard('Eiji')
p(s1)
p('---')

# usando o clear
s1.clear()
p(s1)
p('---')

'''
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # unindo sets
p(s3)
p('---')
s3 = s1 & s2 # intersecção dos sets
p(s3)
p('---')
s3 = s1 - s2 # diferença dos sets
p(s3)
s3 = s2 - s1 # a ordem dos sets faz diferença no resultado
p(s3)
p('---')
s3 = s1 ^ s2 # diferença simétrica dos sets
p(s3)
p('---')