var express = require('express');
var router = express.Router();

router.get("/", function(req, res, next) {
    res.render('pages/home', {pageActive : 'home'});
})

router.get("/pagina1", function(req, res, next) {
    res.render('pages/pagina1', {pageActive : 'pagina1'});
})

router.get("/operacoes", function(req, res, next) {
    res.render('pages/operacoes', {pageActive : 'operacoes'});
})

router.get("/sobre", function(req, res, next) {
    res.render('pages/sobre', {pageActive : 'sobre'});
})

module.exports = router;
