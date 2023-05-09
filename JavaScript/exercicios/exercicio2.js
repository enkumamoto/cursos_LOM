// a o texto deve ter variaveis para ficar dinamico
// Eiji Kumamoto tem 41 anos, pesa 80kg, tem 1.84 de altura e seu IMC eh de 23.63

const nome = 'Eiji' 
const sobrenome = 'Kumamoto'
const idade = 41
const peso = 80
const alturaEmM = 1.84
let IMC = Math.round(peso / (alturaEmM * alturaEmM))
let anoDeNascimento = 2023 - idade

console.log(`${nome} ${sobrenome} tem ${idade} anos, pesa ${peso}kg, tem ${alturaEmM}m de altura e seu IMC eh de ${IMC}.`) // forma mais legivel 
console.log(`${nome} nasceu em: ${anoDeNascimento}`)