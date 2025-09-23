const http = require('http');

//criar servidor

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-type': 'text/plain'});
    res.end('ola, vc esta no meu servidos nodejs');
});

// ouvindo na porta 3000

server.listen(3000, () => {
    console.log("servidor rodando em http://localhost:3000");
})