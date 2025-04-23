// 3)​ Crie um programa que peça ao usuário um número inteiro positivo n e exiba a
// tabuada desse número de 1 a 10 utilizando um loop for.

function mostraTabuada(num) {
    let resultado; 
    for (let i = 1; i <= 10; i++) {
        resultado = `${num} * ${i} = ${num*i}`
        console.log(resultado);
    }
}

mostraTabuada(7);