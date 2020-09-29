const db = require('../../config/database.js');
const listaMarko = require('../views/livros/lista/lista.marko.js');
const LivroDao = require('../infra/livro-dao');

module.exports = (app) => {
    app.get(`/`, function(req, res){
        res.send(
            `<html>
                <body>
                    <h1>teste nodemon</h1>
                </body>
            </html>`
        );
    });

    app.get(`/livros`, function(req, res){
        const livroDao = new LivroDao(db);
        livroDao.lista().then(livros => res.marko(
            require('../views/livros/lista/lista.marko'),
            {
                livros
            }

        )).catch(erro => console.log(erro)); 
    });
}