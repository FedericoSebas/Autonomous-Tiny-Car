require('dotenv').config()

const express = require('express')

const app = express()

app.get('/',(req,res)=>{
  console.log('Peticion recibida')

  res.status(200).send("<h1>Hola mundo con nodemon</h1>")
})

const PORT = process.env.PORT

app.listen(PORT,()=>{
  console.log(`escuchando en el puerto ${PORT}`)
})
