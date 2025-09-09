//manipulação de arquivos (ler,escrever, criar, apagar, etc)

const fs = require('fs');

//criar um arquivo 

fs.writeFileSync('teste.txt', 'ola, esse eh meu primeiro arquivo em Node');

//ler arquivo

const conteudo = fs.readFileSync('teste.txt', 'utf-8');
console,log("conteudo do arquivo: ", conteudo);

//adicionar texto no arquivo sem apagar o anterior

fs.appendFileSync('teste.txt', '\nNova linha adicionada');

// ler novamente

const atualizado = fs.readFileSync('teste.txt', 'utf-8');
console.log("arquivo atualizado: ", atualizado);
