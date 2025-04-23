// 2)​ Faça um script que leia três números inteiros, em seguida mostre o maior e o
// menor deles.


function mostraMaiorMenor(n1, n2, n3) {
    lista = [n1, n2, n3];
    var maior = lista[0];
    for (let i in lista) {
        if (lista[i] > maior) {
            maior = lista[i]
        }
    }

    var menor = lista[0];
    for (let i in lista) {
        if (lista[i] < menor) {
            maior = lista[i]
        }
    }
    return {"maior":maior, "menor": menor}
}

let n1 = 4;
let n2 = 10;
let n3 = 9;

let resultado = mostraMaiorMenor(n1, n2, n3)

console.log(`Maior: ${resultado["maior"]}\nMenor: ${resultado["menor"]}`);

