const http = require("http");

 //criando um servidor
 const server =  http.createServer((req, res) => {
    res.writeHead(200, {'Content-type': 'text/plain'});
    res.end('SERVIDOR CRIADO COM SUCESSO');
 })

 //  ouvindo na porta 3000

server.listen(3000,() => {
    console.log('Servidor rodando em http://localhost:3000')
})