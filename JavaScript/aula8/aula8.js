//diferenca entre var e let
var nome = 'Eiji'
var nome = 'Kumamoto' // desta forma o var redeclara o valor da variavel

console.log(nome)
console.log('---')

/* Se declarar uma variavel da forma abaixo:

nome = 'Eiji'

O JS considera como uma variavel global e isso pode gerar um problema
para o codigo*/

// quando se usa o let para declarar variavel, quer dizer que esta
// variavel nao tera ser valor alterado em algum momento
let outroNome = 'Eiji'
// let outroNome = 'Kumamoto'
console.log(outroNome)
console.log('---')