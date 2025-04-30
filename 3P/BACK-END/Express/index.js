const express = require('express')
const app = express()
const port = 3000
/* O require alem de executar o arquivo, recebe de 
retorno o que ele esportar: um texto, um objeto, um array, etc. */
const router_hello = require('./routes/hello')

/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs')

/* Middleware para servir arquivos estáticos, como CSS e JavaScript */
app.use(express.static('public'))

/*
body-parser é Middleware para fazer o parse do corpo da requisição antes de utilizarmos o req.body
O express.urlencoded() faz o parse do corpo da requisição para o formato URL-encoded.
O valor falso para extended indica que o body-parser vai aceitar somente strings e arrays, enquanto
o valor verdadeiro indica que o body-parser vai aceitar objetos aninhados ou qualquer outro tipo.
*/
app.use(express.urlencoded({extended: false}))

/* Definir que o objeto app, agora direcione todas as 
requisições para a raiz de requisições para o objeto router. */
app.use('/', router_hello)

app.listen(port, () => {
    console.log(`Example app listening on port http://localhost:${port}`)
})