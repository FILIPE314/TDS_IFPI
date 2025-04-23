// 3)​ Implemente uma classe chamada “ContaBancaria” que possua atributos para
// armazenar o número da conta, nome do titular e saldo. Adicione métodos para
// realizar depósitos e saques que recebem como parâmetro o valor.

class ContaBancaria {
    constructor(numeroConta, nomeTitular, saldo) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldo = saldo;
    }
    realizaSaque(valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            return `\nUsuário: ${this.nomeTitular}, número da conta ${this.numeroConta}
Saque realizado com sucesso! Seu saldo é de ${this.saldo}.`;
        } else {
            return `\nUsuário: ${this.nomeTitular}, número da conta ${this.numeroConta}
Saldo insuficiente! não foi possível realizar o saque.`;
        }
    }
    realizaDeposito(valor) {
        this.saldo += valor;
        return `\nDepósito feito com sucesso! O seu saldo é de ${this.saldo}`;
    }
}

const conta1 = new ContaBancaria(1234, "Usuário1", 0);

console.log(conta1.realizaDeposito(60));
console.log(conta1);

console.log(conta1.realizaSaque(50));
console.log(conta1);

console.log(conta1.realizaSaque(10));
console.log(conta1);

const conta2 = new ContaBancaria(3241, 'Usuário2', 8);

