const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

let registrosFeitos = [];
router.get('/historico', (req, res) => {
    res.render('historico', {registrosFeitos: registrosFeitos})
})

router.get('/registro', (req, res) => {
    res.render('registro')
})

router.post('/registro', (req, res) => {
    disciplina = req.body.disciplina;
    nota1 = parseFloat(req.body.nota1);
    nota2 = parseFloat(req.body.nota2);
    media = (nota1 + nota2 )/ 2;
    registro = {
        disciplina : disciplina,
        n1 : nota1,
        n2 : nota2,
        media : media
    }
    registrosFeitos.push(registro);
    res.render('historico', {registrosFeitos});
})
module.exports = router