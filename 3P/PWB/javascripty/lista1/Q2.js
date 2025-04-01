// =============================================================================================================================================================
// Questão 2
function max(num1, num2, num3) {
    if (num1 > num2 & num1 > num3 & num3 > num2) {
        console.log(`Maior número: ${num1}\nMenor número: ${num2}`)
    }
    if (num1 > num2 & num1 > num3 & num3 < num2) {
        console.log(`Maior número: ${num1}\nMenor número: ${num3}`)
    }
    if (num1 < num2 & num1 < num3 & num3 > num2) {
        console.log(`Maior número: ${num3}\nMenor número: ${num1}`)
    }
    if (num1 < num2 & num1 < num3 & num3 < num2) {
        console.log(`Maior número: ${num2}\nMenor número: ${num1}`)
    }
    if (num1 < num2 & num1 > num3 & num3 < num2) {
        console.log(`Maior número: ${num2}\nMenor número: ${num3}`)
    }
    if (num1 > num2 & num1 < num3 & num3 > num2) {
        console.log(`Maior número: ${num3}\nMenor número: ${num2}`)
    }
}
let a = 18
let b = 19
let c = 15
max(a, b, c)