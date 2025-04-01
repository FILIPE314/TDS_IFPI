// =============================================================================================================================================================
// Questão 5
function arrayRepetido(numeros) {
    let numerosUnicos = []
    for (let i = 0; i <= numeros.length - 1; i++) {
        if (!numerosUnicos.includes(numeros[i])) {
            numerosUnicos.push(numeros[i]);
        }
    }
    console.log(numerosUnicos)
}
function main() {
    const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20]
    arrayRepetido(numeros)
}
main()