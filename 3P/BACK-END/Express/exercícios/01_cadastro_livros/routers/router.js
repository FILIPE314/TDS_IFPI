// Todas as rotas devem ser definidas neste arquivo.
const express = require('express')
// Importa a mini aplicação de roteamento do express.
const router = express.Router()

let livros = [];

router.use(express.urlencoded({ extended: false }));

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/livro_form', (req, res) => {
    res.render('livro_form')
})

router.post('/livro', (req, res) => {
    let titulo = req.body.titulo;
    let autor = req.body.autor;
    let ano = Number(req.body.ano);
    let genero = req.body.genero;

    let livro = {
        titulo: titulo,
        autor: autor,   
        ano: ano,
        genero: genero 
    }

    livros.push(livro);

    res.render('livro_resposta', {livros});
})

router.get('/livro_resposta', (req, res) => {
    res.render('livro_resposta', {livros});
})

// Exporta o roteador para ser utilizado em outros arquivos.
module.exports = router;
