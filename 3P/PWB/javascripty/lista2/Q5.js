// Questão 5
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
    constructor(titulo, autor, numeroPaginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.numeroPaginas = numeroPaginas;
    }
}
function main() {
    const cadastroAutor = new Autor('Genivaldo', 'Periondrimo');
    const cadastroLivro = new Livro('Como não ser otário', cadastroAutor.nomeCompleto(), 23);
    console.log(cadastroLivro);
}
main()