const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/nova_operacao', (req, res) => {
    res.render('nova_operacao')
})

router.post('/nova_operacao', (req, res) => {
    let data = req.body.data;
    let codigo = req.body.codigo;
    let tipo = req.body.tipo;
    let quantidade = Number(req.body.quantidade);
    let preco = Number(req.body.preco);
    let valorBruto = quantidade * preco;
    let valorLiquido;

    let lista_operacoes = [];

    // Trata a condição para o resultado do valor líquido
    if (tipo == 'compra') {
        valorLiquido = valorBruto + ((valorBruto * 0.05) /100) 
    } else {
        valorLiquido = valorBruto - ((valorBruto * 0.05) /100) 
    }    
    
    lista_operacoes.push({
        data : data,
        codigo : codigo,
        tipo : tipo,
        quantidade : quantidade,
        preco : preco,
        valorBruto : valorBruto,
        valorLiquido : valorLiquido
    });

    res.render('resposta_operacao', {lista_operacoes : lista_operacoes});    
})

module.exports = router