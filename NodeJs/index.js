console.log("Ola, Node.js!");

function saudacao (nome) {
    return `Ola, ${nome}! Seja bem vindo ao Node.js!!`
}

console.log(saudacao("Endreus"))

const soma = (a, b) => {
    return a + b;
}

console.log(soma(2, 2));


const nomes = (nome,idade) => {
    return `Ola, ${nome}! Vc tem ${idade} anos`; 
}

console.log(nomes("endreus", 21));

/* TRAZENDO DADOS DO ARQUIVO MATEMATICA.JS DO */

const mat = require('./matematica.js');

console.log("resultado da soma :", mat.soma(5,3));
console.log("resultado da multiplicaçao : ", mat.multiplicar(3,8));
console.log("resultado da subtraçao: ", mat.subtrair(10,4));
console.log("resultado da divisão: ", mat.dividir(20, 10));


/* ================================================= */


/*TRAZENDO DADOS DO ARQUIVO MENSAGEM.JS*/

const mens = require('./mensagem.js');

console.log(mens.boasvindas("ENDREUS"));
console.log(mens.despedida("ENDREUS"));
console.log(mens.elogio("ENDREUS"));