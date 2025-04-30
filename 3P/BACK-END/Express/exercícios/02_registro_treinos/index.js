const express = require('express')
const app = express()
const port = 3000

const router = require('./routers/router.js')
app.use(express.static('public'))


app.set('views', 'views')
app.set('view engine', 'ejs')
// app.use(express.urlencoded({extended: false}))


app.use('/', router)

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})

