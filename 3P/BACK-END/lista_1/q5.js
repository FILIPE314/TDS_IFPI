// 5)​ Dado o array numeros, crie um novo array chamado numerosUnicos, contendo
// os mesmos elementos do array original, mas sem valores repetidos e exibir no
// console.
// ​
// const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

function removeRepetido(numeros) {
    let numerosUnicos = [];

    for (let i = 0; i < numeros.length; i++) {
        if (!numerosUnicos.includes(numeros[i])){
            numerosUnicos.push(numeros[i]);
        }
        continue;
    }
    return numerosUnicos
}

let numerosUnicos = removeRepetido(numeros);

console.log(numerosUnicos);

