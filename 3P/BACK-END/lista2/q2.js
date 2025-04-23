// 2)​ Implemente uma classe chamada “Aluno” que possua atributos para armazenar o
// nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média
// das notas e verificar a situação do aluno (aprovado ou reprovado) de acordo com
// as regras de onde você estuda ou estudou.

class Aluno{
    constructor(nome, matricula, nota1, nota2){
        this.nome = nome;
        this.matricula = matricula;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    getMedia(){
        return (this.nota1 + this.nota2) / 2;
    }
    getSituacao() {
        if (this.getMedia() >= 7) {
            return`Você foi aprovado!! Sua média foi ${this.getMedia()}`;
        }
        return `Você foi reprovado!! Sua média foi ${this.getMedia()}`;
    }
}

const aluno1 = new Aluno("Joaozin", "1333", 5, 4);

console.log(aluno1.getMedia());
console.log(aluno1.getSituacao());

