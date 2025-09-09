//informaçoes do sistema operacional

const os = require('os');

console.log("Sistema operacional", os.type());
console.log("versao", os.release());
console.log("memoria local (MB)", os.totalmem() / 1024/ 1024);
console.log("memoria livre (MB)", os.freemem() /1024 / 1024);
console.log("tempo de atividade (segundos)", os.uptime());

console.log("nome do usuario atual: ", os.userInfo());
console.log("numero de CPUs no computador: ", os.cpus().length)
