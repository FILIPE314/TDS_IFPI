// 4)​ Adicione na classe da questão anterior o método para realizar transferência entre
// contas, que recebe como parâmetros uma conta e o valor a ser transferido.

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
    realizaTrasferencia(contaDestino, valor) {
        if (valor > this.saldo) {
            console.log("\nSaldo insuficiente!");
        }else {
            this.saldo -= valor;        
            console.log(`Transferência realizada com sucesso! Saldo atual: ${this.saldo}`); 
        }

        // try {
        //     if (isNaN(valor)) throw "Caractere inválido, digite um número";

        //     if (typeof valor == "number" && valor <= this.saldo){
        //         contaDestino.realizaDeposito(valor);
        //         this.saldo -= valor;        
        //         console.log(`Transferência realizada com sucesso! Saldo atual: ${this.saldo}`);        
        //     }
            
            
        // } catch (erro){
        //     console.log(erro)
        // }
    }
}

const conta1 = new ContaBancaria(1234, "Usuário1", 60);
const conta2 = new ContaBancaria(3214, "Usuário2" ,40)




// console.log(conta1);
// console.log(conta2);

conta1.realizaTrasferencia(conta2, 20)

// console.log(conta1);
// console.log(conta2);

// conta1.realizaTrasferencia(conta2, 50)
