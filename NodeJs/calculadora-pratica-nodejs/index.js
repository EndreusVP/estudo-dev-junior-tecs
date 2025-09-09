const calculadora = require('./calculadora');

console.log("digite um numero");

let num1 = 10;

console.log("digite outro numero");

let num2 =  2;

console.log("qual operção vc quer fazer?");
console.log("1 - soma")
console.log("2 - subtrair")
console.log("3 - multiplicar")
console.log("4 - dividir")

let operacao = 1;

switch (operacao) {
    case 1:
        console.log(`A soma de ${num1} e ${num2} eh: `, calculadora.somar(num1,num2))
        break;
    case 2:
        console.log(`A subtração entre ${num1} e ${num2} eh: `, calculadora.subtrair(num1,num2))
        break;
    case 3:
        console.log(`A multiplicação entre ${num1} e ${num2} eh: `, calculadora.multiplicar(num1,num2));
        break;
    case 4:
        console.log(`A divisão entre ${num1} e ${num2} eh: `, calculadora.dividir(num1,num2))
    default:
        break;
}
