// Questão 2
class Aluno {
    constructor(nome, matricula, nota1, nota2) {
        this.nome = nome;
        this.matricula = matricula;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    media() {
        if (this.nota1 >= 0 && this.nota2 >= 0) {
            let result = (this.nota1 + this.nota2) / 2;
            return result
        } else {
            return `Digite uma nota válida!`
        }
    }
    aprovadoOuReprovado() {
        if (this.media() >= 6) {
            return `Aluno ${this.nome} aprovado!`
        } else if (this.media() < 6) {
            return `Aluno ${this.nome} reprovado!`
        } else {
            return this.media();
        }
    }
}
function main() {
    const cadastro1 = new Aluno('Josivaldo', '123josi', -1, 10);
    console.log(cadastro1.aprovadoOuReprovado());
}
main();