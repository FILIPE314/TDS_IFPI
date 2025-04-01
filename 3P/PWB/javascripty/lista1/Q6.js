// =============================================================================================================================================================
// Questão 6
function media(notas) {
    let result = 0;
    for (let i = 0; i <= notas.length - 1; i++) {
        result += notas[i]
    }
    return `Sua média é ${result / notas.length}`
}
function main() {
    let notas = [5, 5, 5, 5, 5];
    console.log(media(notas));    
}
main()