const express = require('express');
const app = express();

const rotas = require('../app/rotes/router.js');
rotas(app);

module.exports = app;