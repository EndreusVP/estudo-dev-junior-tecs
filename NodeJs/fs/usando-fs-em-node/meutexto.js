const fs = require('fs');

fs.writeFileSync('meu-texto', 'estou aprendendo NodeJs');

const lerArquivo = fs.readFileSync('meu-texto', 'utf-8');
console.log("lendo arquivo: ", lerArquivo);

fs.appendFileSync('meu-texto', '\nNode.JS eh mto legal');

lerArquivo = fs.readFileSync('mmeu-texto', 'utf-8');
console.log("lendo o arquivo atualizado: ", lerArquivo); 