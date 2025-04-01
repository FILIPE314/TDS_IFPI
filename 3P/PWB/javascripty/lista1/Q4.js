// =============================================================================================================================================================
// Questão 4
function calcularPop(popA, popB) {
    let anos = 0;
    for (let i = 1; popA <= popB; anos++) {
        popA += popA * 0.03;
        popB += popB * 0.015;
    }
    console.log(`${anos}`)
}
function main() {
    let popA = 80000;
    let popB = 200000;
    calcularPop(popA, popB)
}
main()