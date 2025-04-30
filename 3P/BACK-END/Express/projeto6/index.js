const express = require('express')
const app = express()
const port = 3000
const router_hello = require('./routers/hello.js')

/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs');

/* Middleware para servir arquivos estáticos, como CSS e JavaScript */
app.use(express.static('public'))

app.use(express.urlencoded({extended: false}))

app.use('/', router_hello)

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})