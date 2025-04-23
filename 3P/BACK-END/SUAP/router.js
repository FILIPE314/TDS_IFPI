const express = require('express')
const { listenerCount } = require('process')
const router = express.Router()

listFaturamentos = []

router.get('/', (req, res) => {
  res.send('Hello World!')
})

router.get('/form', (req, res) => {
    res.render('form')
})

router.post('/resposta', (req, res) => {
    const codigo = req.body.codigo;
    const data = req.body.data;
    const quantidade = parseInt(req.body.number_int);
    const preco = parseFloat(req.body.number_float);
    const tipo = req.body.tipo;
    let valorBruto = quantidade * preco;
    let valorLiquido;

    if (tipo == "Compra") {
        valorLiquido = valorBruto + (valorBruto * 0.0005)
    } else if (tipo == "Venda") {
        valorLiquido = valorBruto - (valorBruto * 0.0005)
    }

    const coisas = [codigo, data, tipo, quantidade, preco, valorBruto, valorLiquido]

    listFaturamentos.push(coisas)

    res.render('resposta', {
        listFaturamentos: listFaturamentos
    })
})

module.exports = router