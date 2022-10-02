const express = require('express')

const app = express()

app.get('/',(req,res)=>{
  console.log('Peticion recibida')

  res.status(200).send("<h1>Hola mundo con nodemon</h1>")
})

app.listen(4000,()=>{
  console.log("escuchando en el puerto 4000")
})