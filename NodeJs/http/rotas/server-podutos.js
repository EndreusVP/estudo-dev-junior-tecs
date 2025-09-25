const http = require('http')
let lista_produtos = ["maça", "uva", "pera"]

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        res.writeHead(200, { "Content-Type": "text/html" })
        res.end("<h1>Pagina inicial</h1><p>Voce esta na Pagina Inicial</p>")
    } else if (req.url === "/produtos") {
        res.writeHead(200, { 'Content-type': 'text/html' })

        let listaHTML = "<ul>"

        for(let i = 0; i < lista_produtos.length; i++){
            listaHTML += `<li>${lista_produtos[i]}</li>`
        }

        listaHTML += "</ul>"

        res.end(`<h1>Meus Produtos</h1> ${listaHTML}`)
    } else if (req.url === "/servicos") {
        res.writeHead(200, { 'Content-type': 'text/html' })
        res.end("<h1>Serviços</h1><p>Esses são meus serviços: </p>")
    } else {
        res.writeHead(404, { 'Content-type': 'text/html' })
        res.end("<h1>ERR 404</h1><p>Erro ao encontrar a pagina</p>")
    }
})

server.listen(3000, () => {
    console.log("esta usando o http://localhost:3000")
})