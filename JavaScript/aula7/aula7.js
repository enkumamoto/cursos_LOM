// regras para variaveis
// nao podemos criar constante com palavras reservadas
// constantes precisam ter nomes significativos
// nao pode comecar com nome de uma constante com numero
// nao podem conter espacos ou tracos
// utilizamos camelCase
// variaveis sao case-sensitive
// nao podemos modificar o valor da constante
// nao utilize var, utilize const

const pai = 'Joao' //string - texto
// pai = 'Jose' // a redeclaracao de valor em constante gera erro, diferente do let
console.log(pai)
console.log('---')

// atribuindo uma constante como valor de uma outra variavel
const primeiroNumero = 5 // numero, mas se colocar entre aspas passa a ser string
const segundoNumero = 10
const resultado = primeiroNumero * segundoNumero
console.log(resultado)
console.log('---')

const resultadoDuplicado = resultado * 2
console.log(resultadoDuplicado)
console.log('---')

let resultadoTriplicado = resultado * 3 // mostrando a troca do valor dentro do let
resultadoTriplicado = resultado + 5
console.log(resultadoTriplicado)
console.log('---')

// caso coloque aspas num numero, o javascript reconhece como string, mesmo que concatene com numero
const oPrimeiroNumero = '5'
const oSegundoNumero = 10
const outroResultado = oPrimeiroNumero + oSegundoNumero
console.log(typeof (oPrimeiroNumero+oSegundoNumero))
console.log(outroResultado)
console.log('---')