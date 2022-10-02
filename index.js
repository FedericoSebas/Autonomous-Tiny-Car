const express = require('express')

const app = express()

app.get('/',(req,res)=>{
  console.log('Peticion recibida')

  res.status(200).send("<h1>Hola mundo con nodemon</h1>")
})

const PORT = process.env.PORT || 4000

console.log({PORT})

app.listen(PORT,()=>{
  console.log("escuchando en el puerto 4000")
})
