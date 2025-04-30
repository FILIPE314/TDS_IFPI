// Todas as rotas devem ser definidas neste arquivo.

const express = require('express')
// Importa a mini aplicação de roteamento do express.
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/ola_form', (req, res) => {
    res.render('ola_form')
})

router.post('/ola', (req, res) => {
    nome = req.body.nome;
    res.render('ola_resposta', {nome : nome})
})

router.get('/ola_resposta', (req, res) => {
    res.render('ola_resposta')
})


module.exports = router