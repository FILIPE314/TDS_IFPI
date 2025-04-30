const express = require('express')
const app = express()
const port = 3000

app.set('views', 'views');
app.set('view engine', 'ejs');


app.use(express.urlencoded({extended: false}));

app.get('/', (req, res) => {
  res.render('home');
})

app.get('/carlos', (req, res) => {
  res.send('Olá Carlos!');
})

app.get('/home', (req, res) => {
  res.send('Minha página!');
})

app.listen(port, () => {
  console.log(`App de exemplo esta rodando no endereço http://localhost:${port}/`);
})

app.post('/resposta_ola', (req, res) => {
    let nome = req.body.nome;
    res.send(`Olá ${nome}, como você está?`);
})

app.get("/ola", (req, res) => {
  res.send(`
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Olá</h1>
    <form action="/resposta_ola" method="post">
        <label for="inome">Nome</label>
        <input type="text" id="inome" name="nome">
    </form>
</body>
</html>`);
});

