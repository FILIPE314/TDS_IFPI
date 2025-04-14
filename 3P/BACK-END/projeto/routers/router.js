const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

router.get('historico', (req, res) => {
    res.render('historico')
})




module.exports = router