// 5)​ Implemente uma classe “Autor” que possui como atributos o nome e sobrenome do
// autor e criar um método que imprima o nome completo (nome + sobrenome).
// Implemente uma classe chamada “Livro” com atributos para armazenar o título, o
// autor e o número de páginas do livro.

class Autor {
    constructor(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    getNome() {
        return `${this.nome} ${this.sobrenome}`;
    }
}

class Livro {
    constructor(titulo, autor, numeroPaginas) {
        this.titulo = titulo;
        this.autor = autor.getNome();
        this.numeroPaginas = `${numeroPaginas} páginas`;
    }    
}

const autor1 = new Autor("Jairo", "Jonson");

const livro1 = new Livro("As crônicas de Junior", autor1, 35);

console.log(livro1);