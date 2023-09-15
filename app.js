const express = require('express');
const path = require("path");

const app = express();

//implementando o requiriendo las rutas
const registerRoutes = require('./routes/registerRoutes');
const loginRoutes = require('./routes/loginRoutes');

//definiendo las rutas
app.use('/login', loginRoutes);
app.use('/register', registerRoutes);

app.listen(3000, () =>
    console.log("Levantando un servidor con Express")
);