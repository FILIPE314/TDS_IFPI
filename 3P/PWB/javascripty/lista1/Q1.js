// =============================================================================================================================================================
// Questão 1 letra a e b
function testeEscopo() {
    var a = 10;
    let b = 20;
    const c = 30;
    if (true) {
        var a = 40;
        let b = 50;
        const c = 60;
        console.log(a, b, c);
    }
    console.log(a, b, c);
}
testeEscopo()
// Resposta a) 40 50 60
// Resposta b) 40 20 30