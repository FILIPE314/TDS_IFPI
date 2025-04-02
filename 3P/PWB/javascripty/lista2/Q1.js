// Questão 1
class Circulo {
    constructor(raio) {
        this.raio = raio
    }
    perimetro() {
        let result = 2 * this.raio * 3.14;
        return result
    }
    area() {
        let result = 3.14 * (this.raio ** 2);
        return result
    }
}
function main() {
    const raio = new Circulo(18);
    console.log(`Perímetro do círculo: ${raio.perimetro().toFixed(2)}`);
    console.log(`Área do círculo: ${raio.area()}`);
}
main();