// Questão 6
class Autor {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }
    nomeCompleto() {
        if (this.nome != `` && this.sobrenome != ``) {
            return `Autor: ${this.nome} ${this.sobrenome}`
        } else {
            return `Nome inválido, procure outro nome`
        }
    }
}
class Livro {
    constructor(titulo, autor = [], numeroPaginas = 0) {
        this.titulo = titulo;
        this.autor = autor;
        this.numeroPaginas = numeroPaginas;
    }
}
function main() {
    const cadastroAutor1 = new Autor('Genivaldo', 'Periondrimo');
    const cadastroAutor2 = new Autor('Gato', 'Xoxo');
    const cadastroLivro = new Livro('Como não ser otário', [cadastroAutor1.nomeCompleto(), cadastroAutor2.nomeCompleto()], 23);
    console.log(cadastroLivro);
}
main()