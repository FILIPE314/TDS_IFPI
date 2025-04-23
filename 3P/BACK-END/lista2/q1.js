// Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio
// e métodos para calcular a área e o perímetro do círculo.

class Circulo{
    constructor(raio){
        this.raio = raio;
    }
    getArea() {
        return 3.14 * this.raio **2;
    }
    getPerimetro(){
        return 3.14 * this.raio * 2;
    }
}

const circulo1 = new Circulo(5);

console.log(circulo1.getArea());

console.log(circulo1.getPerimetro().toFixed(2));

