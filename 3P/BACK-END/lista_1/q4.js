// 4)​ Supondo que a população de um país A seja da ordem de 80000 habitantes com
// uma taxa anual de crescimento de 3% e que a população de B seja 200000
// habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
// e escreva o número de anos necessários para que a população do país A
// ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

let paisA = 80000
let paisB = 200000

function taxaCrescimentoAB(populacaoA, populacaoB){
    let anos = 0;
    pA = populacaoA;
    pB = populacaoB;
    while (pA < pB) {
        pA += pA * 0.03;
        pB += pB * 0.015;
        anos ++;        
    }
    return anos
}

resultado = taxaCrescimentoAB(paisA, paisB);

console.log(`A população do país A irá ultrapassar ou igualar a população do país B em ${resultado} anos!`);

