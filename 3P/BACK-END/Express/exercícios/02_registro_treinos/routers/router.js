// Todas as rotas devem ser definidas neste arquivo.
const express = require('express');
// Importa a mini aplicação de roteamento do express.
const router = express.Router();

let treinos = [];

router.use(express.urlencoded({ extended: false }));

router.get('/', (req, res) => {
    res.render('home');
})

router.get('/registro', (req, res) => {
    res.render('registro');
})

router.post('/registro', (req, res) => {
    let dia = req.body.dia;
    let nome = req.body.nome;
    let duracao = Number(req.body.duracao);

    const treino = {
        dia: dia,
        nome: nome,
        duracao: duracao
    }

    if (treinos.length > 0) {
        for (let i = 0; i < treinos.length; i++) {
            if (treinos[i] != treino) {
                treinos.push(treino)
                res.render('resposta_registro', {treinos});
            } 
        }
    } else {
        treinos.push(treino)
        res.render('resposta_registro', {treinos});
    }
    
})

router.get('/resposta_registro', (req, res) => {
    res.render('resposta_registro', {treinos});
})



module.exports = router;