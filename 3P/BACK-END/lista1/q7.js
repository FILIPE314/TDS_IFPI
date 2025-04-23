// 7)​ Desenvolva uma função que verifique se uma palavra é um palíndromo (lê-se da
//     mesma forma da esquerda para a direita e vice-versa). Retorne true se for um
//     palíndromo e false se não for.


function verificaPalindromo(palavra) {
    let palavraSeparada = palavra.split("");
    let inverso = palavraSeparada.reverse();
    let palavraInvertida = inverso.join("");
    
    if (palavraInvertida == palavra){
        return true
    } else{
        return false;
    }
    
}

let palavra1 = "CASACO";
let palavra2 = "ARARA";
let palavra3 = "RADAR";

console.log(verificaPalindromo(palavra1));
console.log(verificaPalindromo(palavra2));
console.log(verificaPalindromo(palavra3));




