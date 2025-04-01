// =============================================================================================================================================================
// Questão 7
function palindromo(palavra) {
    let palavraInvertida = "";
    for (let i = palavra.length - 1; i >= 0; i--) {
        palavraInvertida += palavra[i];
    }
    if (palavraInvertida == palavra) {
        return true
    } else {
        return false
    }
}
function main() {
    let palavra = "ovo"
    console.log(palindromo(palavra));
}
main()