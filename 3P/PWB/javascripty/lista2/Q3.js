// Questão 3
class ContaBancaria {
    constructor(numeroConta, nomeTitular, saldoConta) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldoConta = saldoConta;
    }
    deposito(entrada) {
        if (entrada > 0) {
            this.saldoConta += entrada;
            return `Seu saldo é R$ ${this.saldoConta.toFixed(2)}`
        } else {
            return `Valor inválido!`
        }
    }
    saque(saida) {
        if (saida > this.saldoConta) {
            return `Saldo indisponível! Vai trabalhar vagabundo, quer levar vantagem é?`
        } else if (saida > 0) {
            this.saldoConta -= saida;
            return `Seu saldo é R$ ${this.saldoConta.toFixed(2)}`
        } else {
            return `Valor inválido!`
        }
    }
}
function main() {
    const cadastro1 = new ContaBancaria(4545, 'Adalberto', 350.00);
    console.log(cadastro1.saque(20));
    console.log(cadastro1.deposito(1020));
    console.log(cadastro1.saque(2000));
}
main()