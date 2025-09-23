const http = require("http");

// criando server 
const server = http.createServer((req, res) => {
    if (req.url === "/") {
        res.writeHead(200, { 'Content-Type': 'text/html' })
        res.end('<h1>Pagina Inicial</h1><p>Essa eh a pagia inicial do server</p>')
    } else if(req.url === "/sobre"){
        res.writeHead(200, {'Content-Type' : 'text/html'});
        res.end('<h1>Sobre</h1><p>Sobre a empresa</p>');
    } else if (req.url === "/contato") {
        res.writeHead(200, {'Content-Type' : 'text/html'});
        res.end('<h1>Contato</h1><p>Contate-nos</p>');
    } else {
        res.writeHead(404, {'Content-Type' : 'text/html'})
        res.end('<h1>ERR</h1><p>Pagina nao encontrada</p>')
        
    }
})

//ouvindo a porta 3000
server.listen(3000, () => {
    console.log('Servidor rodando em http://localhost:3000')
})