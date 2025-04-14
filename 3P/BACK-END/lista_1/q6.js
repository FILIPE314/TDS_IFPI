// 6)​ Implemente uma função que recebe como parâmetro um array de números, calcule
// a média aritmética e retorne o resultado.

const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

function calMedia(listaNumeros){
    let numeros = listaNumeros;
    let soma = 0;
    for(let i=0;i<numeros.length;i++){
        soma += numeros[i]

    }
    media = soma / numeros.length;
    return `A média dos números da lista [${numeros}] é: ${media}.`;
}

console.log(calMedia(numeros));
