// Questão 4
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
    transferencia(pix, contaDestino) {
        if (pix > this.saldoConta) {
            return `Saldo indisponível! Vai trabalhar vagabundo, quer levar vantagem é?`
        } else if (pix > 0) {
            this.saldoConta -= pix;
            contaDestino.saldoConta += pix;
            return `Transferência realizada com sucesso para ${contaDestino.nomeTitular} no valor de R$ ${pix.toFixed(2)}\n
                    Seu saldo é R$ ${this.saldoConta.toFixed(2)}\n2`
        } else {
            return `Valor inválido!`
        }
    }
}
function main() {
    const cadastro1 = new ContaBancaria(4545, 'Adalberto', 350.00);
    const cadastro2 = new ContaBancaria(1212, 'Gato xoxo capenga', 500.00);
    console.log(cadastro1.transferencia(20, cadastro2));
    console.log(cadastro2.transferencia(1000, cadastro1));
}
main()