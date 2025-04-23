// CRIAÇÃO DE CLASSE

class Aluno{
    constructor(matricula, nome, media = 0){
        this.matricula = matricula;
        this.nome = nome;
        this.notaBimestral1 = 0;
        this.notaBimestral2 = 0;
    }
    getMedia() {
        return (this.notaBimestral1 + this.notaBimestral2) / 2;
    }
};

const aluno1 = new Aluno(1234, "Joaozin");
// codigo para mostrar a matrícula do aluno:
// console.log(aluno1.matricula);

aluno1.notaBimestral1 = 6;
aluno1.notaBimestral2 = 10;

console.log(aluno1.getMedia());


