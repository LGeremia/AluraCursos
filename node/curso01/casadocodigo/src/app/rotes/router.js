module.exports = (app) => {
    app.get(`/`, function(req, res){
        res.send(
            `<html>
                <body>
                    <h1>teste</h1>
                </body>
            </html>`
        );
    });

    app.get(`/livros`, function(req, res){
        res.send(
            `<html>
                <body>
                    <h1>Livros</h1>
                </body>
            </html>`
        );
    });
}