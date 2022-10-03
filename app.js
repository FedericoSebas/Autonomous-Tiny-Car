require('dotenv').config()

const express = require('express')

const app = express()

const path = require('path')

const mongoose = require('mongoose')

mongoose.connect(
  `mongodb+srv://federico:${process.env.MONGO_DB_PASS}@cluster0.pp8srvh.mongodb.net/stock-app?retryWrites=true&w=majority`
  )
  .then((result) => {
      app.listen(process.env.PORT,()=>{
        console.log(`escuchando en el puerto ${process.env.PORT}`)
      })
      console.log("Conexion exitosa a la BBDD")
    })
    .catch((err) => console.log(err))
    
const productSchema = mongoose.Schema(
  {
    name: { type: String, required: true },
    price: Number,
  },
  { timestamps: true }
)

const Product = mongoose.model('Product', productSchema)
    
app.use(express.json())

app.post('/api/v1/products',(req,res)=>{
  const newProduct = new Product(req.body)

  newProduct
  .save()
  .then((result) => {
    res.status(201).json({ ok: true })
  })
  .catch((e) => console.log(e))
})

app.use(express.static(path.join(__dirname,'public')))

