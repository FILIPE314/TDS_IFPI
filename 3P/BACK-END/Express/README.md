# Tutorial para a disciplina de Programação Web Back-End período 2025-1

## 1 - Requisitos do ambiente

1. Node v22.14.0
[Instalação do node](https://nodejs.org/pt/download).
Seguir os passos de acordo com o Sistema Operacional utilizado.

2. NPM 10.9.2
Normalmente é instalado junto com o Node.

3. Se for seguir o tutorial a partir de uma outra parte do tutorial que não a inicial, mudar para a branch desejada, baixar o projeto e no nível raiz do projeto (o mesmo do arquivo package.json) executar o comando:

```bash
npm install
```

Isso irá instalar todas as dependências para o projeto.

## 2 - Criaçao do projeto Hello World com Express

Executar os comandos:

1. criação do arquivo de configuração do projeto.

```bash
npm init --yes
```

2. instalação framework express.

```bash
npm install express
```

3. Acessar [Express](https://expressjs.com/) para código de hello world e documentação.
Copiar o código de "hello world" do site e colar no arquivo index.js

```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})

```

4. Instação e configuração do Nodemon
Evitar ter que ficar parando e reiniciando o servidor a cada alteração no projeto.

```bash
npm install nodemon
```

Acrescentar o script de inicialização na configuração.
No arquivo package.json adicionar o script de start. Altere a propriedade "scripts" para ficar como a seguir:

```javascript
"scripts": {
    "start": "nodemon",
    "test": "echo \"Error: no test specified\" && exit 1"
},
```

A partir de agora para iniciar o projeto iremos utilizar o comando

```bash
npm start
```

## 3 - Início ao tratamento de requisições com parâmetros

1. Criar uma nova função para tratamento de requisiçoes do tipo post com parâmetro.
Criar a função no arquivo index.js logo abaixo da função para requisição do hello world!

```javascript
app.post('/ola', (req, res) => {
    // req.body é um objeto que contém os dados enviados no corpo da requisição
    nome = req.body.nome // recupera o valor do parametro com chave = nome
    res.send(`Olá ${nome}`)
})
```

2. Configurar o formato de parser utilizado pelo middleware body-parser.
Para que a instrução que recupera o nome do corpo da requisição funcione é preciso definir o formato de parser a ser feito pelo body-parser.
Adicionar a seguinte configuração logo acima das funções de tratamento de requisições.

```javascript
/*
body-parser é Middleware para fazer o parse do corpo da requisição antes de utilizarmos o req.body.
O express.urlencoded() faz o parse do corpo da requisição para o formato URL-encoded.
O valor falso para extended indica que o body-parser vai aceitar somente strings e arrays, enquanto
o valor verdadeiro indica que o body-parser vai aceitar objetos aninhados ou qualquer outro tipo.
*/
app.use(express.urlencoded({extended: false}))
```

3. Utilizar o postman para testar a função.
Ao criar uma nova requisição no postman, escolher o tipo POST e na aba de parâmetros escolher "body" e em seguida o formato
x-www-form-urlencoded para o formato de envio dos parâmetros.

![Postman - Exemplo de requisição do tipo POST com parâmetro.](https://lh3.googleusercontent.com/d/1MerylzOrFyJIULJT4cG5PR_WygxMjheC=s900?authuser=0 "Requisição com Postman")

## 4 - Adição de Views ao projeto

1. Criar uma pasta chamada "views" no nível raiz do projeto.

2. No arquivo de execução do projeto (index.js) definir o valor da propriedade do app que indica o local das views.

```javascript
/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
```

3. Logo abaixo da instrução anterior, definir o valor da propriedade do app que indica qual engine -- motor de construção das páginas dinâmicas -- será utilizado.

```javascript
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs')
```

4. Instalar o EJS

```bash
npm install ejs
```

A partir daqui, para retornar views iremos utilizar o comando a seguir:

```javascript
req.render("nome_do_template_ejs")
```

obs.: o path para o template deve ser considerado a partir do nível da pasta views.

5. Criar dentro da pasta views um template EJS com o nome "ola_form.ejs" e criar um formulário para receber o nome do usuário visitante.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorial - Olá</title>
</head>
<body>
    <div>
        <h1>Formulário de Visitação</h1>
    </div>
    <div>
        <form action="/ola" method="post">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" required>
            <br><br>
            <button type="submit">Enviar</button>
        </form>
    </div>
</body>
</html>
```

6. Criar uma função para tratar a requisição do tipo GET para a view do formulário.

```javascript
app.get('/ola_form', (req, res) => {
    res.render('ola_form')
})
```

7. Executar o projeto e testar acessando a view do formulário.

[http://localhost:3000/ola_form](http://localhost:3000/ola_form)

8. Criar um novo template EJS com o nome "ola_resposta.ejs" na pasta "views" para responder um olá persnalizado ao visitante.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorial - Olá (Resposta)</title>
</head>
<body>
    <div>
        <h1>Resposta ao Visitante</h1>
    </div>
    <div>
        <span>Olá, <%= nome %>!</span><br>
        <span>Obrigado por visitar nosso site.</span>
    </div>
</body>
</html>
```

9. Alterar o método que trata a requisição do tipo POST para "/ola" para retornar o template de resposta renderizado com a informação do formulário.

```javascript
app.post('/ola', (req, res) => {
    // req.body é um objeto que contém os dados enviados no corpo da requisição
    nome = req.body.nome // recupera o valor do parametro com chave = nome
    res.render('ola_resposta', {nome: nome}) // renderiza a view ola_resposta.ejs e passa o valor do nome através de um objeto javascript
})
```

10. Testar novamente acessando o formulário e submetendo o nome do visitante através do botão.

[http://localhost:3000/ola_form](http://localhost:3000/ola_form)

### 4.1 - Exercício

Criar um projeto contendo uma página que recebe dois números através de um formulário, submete os números e exibe o resultado da soma entre esses números em uma página de resposta.

## 5 - Roteamento

1. criar o arquivo "router.js" no nível raiz do projeto.

Importar o express e criar a miniaplicação de roteamento do express.

```javascript
const express = require('express')
const router = express.Router()
```

2. No final do arquivo, exportar o roteador para poder ser utilizado em outros arquivos.

```javascript
module.exports = router
```

3. Trazer as funções de roteamento do "index.js" para o arquivo de rotas e fazer o ajuste no objeto que controla as requisições (antes o objeto app) para o router, conforme exemplo abaixo.

```javascript
// antes no arquivo index.js
// app.get('/', (req, res) => {
//     res.send('Hello World!')
// })
// agora no aquivo router.js
router.get('/', (req, res) => {
    res.send('Hello World!')
})
```

4. Importar os objetos e funções exportadas pelo roteador.

No arquivo "index.js" adicionar a importação antes das definições "set" e "use".

```javascript
const router = require('./router')
```

1. Fazer com que o app agora redirecione todas as requisições do projeto para o roteador (objeto router).

Adicionar a definição de uso antes do "listen" (execução do app).

```javascript
app.use('/', router)
```

### 5.1 - Exercício

1. Criar um aplicação que contem uma página com um formulário (método POST) similar ao da imagem abaixo para cadastrar operações de compra e venda na bolsa de valores do Brasil.

<div align="center">

![Modelo de formulário para o exercício](https://lh3.googleusercontent.com/d/1OjHO0WJpUMGNOQFJydWH8Cb8xC6C1ghR=s250?authuser=0 "Requisição com Postman")

</div>

<ul>
    <li>Criar dois exemplos de códigos: ITSA4 e BBSE3 no select</li>
    <li>Quantidade deve ser um número inteiro</li>
    <li>Preço deve ser um número float</li>
</ul>

1. Definir a ação do formulário para uma função que trata os dados submetidos pelo formulário, cria um objeto javascript e o insere em uma lista.
   
2. Criar uma página que contém um tabela que lista todos as operações salvas na lista.

3. Desafio: após o passo 2, redirecionar para a página que lista as operações.

## 6 - Arquivos estáticos

1. Criar a pasta "public" no nível raiz do projeto.

<ul>
    <li>Criar a subpasta "images"</li>
    <li>Criar a subpasta "javascripts</li>
    <li>Criar a subpasta "stylesheets"</li>
</ul>

2. Configura o middleware do express para informar onde estão os arquivos estáticos.

No arquivo "index.js" adicionar a configuração de uso do express:

```javascript
app.use(express.static('public'))
```

3. A partir daqui, para os arquivos estáticos, utilizar o path relativo ao diretório "public"

Exemplo: utilizar o arquivo "hello.css" localizado em "/public/stylesheets/hello.css"

```html
<link rel="stylesheet" href="/stylesheets/hello.css">
```

### 6.1 - Exercício

Criar o arquivo "estilo.css" no local adequado para personalizar os formulários( e.g. seus labels e inputs e fontes) e aplicar esse estilo na view "ola_form".