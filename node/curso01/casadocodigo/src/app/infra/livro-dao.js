class LivroDao{
    constructor(db){
        this._db = db;
    }
    lista(){
        return new Promise((resolve,reject) =>{
            this._db.all(
                'SELECT * FROM livros',
                (erro, resultados)=>{
                    if (erro) return reject("Não foi possĩvel listar os Livros!")
                    return resolve(resultados);
                });
        });
    }
    adiciona(livro){
        return new Promise((resolve,reject) =>{
            this._db.run(`
                INSERT INTO livros(
                    titulo,
                    preco,
                    descricao
                ) values (?,?,?)
            `,
            [
                livro.titulo,
                livro.preco,
                livro.descricao
            ],
            function(err){
                if(err){
                    console.log(err);
                    return reject('Não foi possível adicionar o livro!')
                }
                resolve();
            }
            );
        });
    }
    consulta(livro){
        return new Promise((resolve,reject) =>{
            this._db.run(`
                SELECT * FROM livros WHERE id = ?
            `,
            [
                livro.id
            ],
            function(err){
                if(err){
                    console.log(err);
                    return reject('Não foi possível adicionar o livro!')
                }
                resolve();
            }
            );
        });
    }
    consulta(livro){
        return new Promise((resolve,reject) =>{
            this._db.run(`
                DELETE FROM livros WHERE id = ?
            `,
            [
                livro.id
            ],
            function(err){
                if(err){
                    console.log(err);
                    return reject('Não foi possível adicionar o livro!')
                }
                resolve();
            }
            );
        });
    }
}

module.exports = LivroDao;