// Letra a
var b1 = document.getElementById('b1');
b1.addEventListener('click', clickb1);

function clickb1() {
    let ct1 = document.getElementById('ct1').value;
    let ct2 = document.getElementById('ct2').value;
    var p1 = document.getElementById('p1');
    p1.innerHTML = ct1 + ' ' + ct2;
}
// Letra b
var b2 = document.getElementById('b2');
b2.addEventListener('click', clickb2);

function clickb2() {
    let ct3 = parseInt(document.getElementById('ct3').value);
    let ct4 = parseInt(document.getElementById('ct4').value);
    var p2 = document.getElementById('p2');
    var soma = ct3 + ct4
    p2.innerHTML = 'Soma: ' + soma + '<br>Diferença: ' + ct3 / ct4;
}
// Letra c
var b3 = document.getElementById('b3');
b3.addEventListener('click', clickb3);

function clickb3() {
    document.getElementById('ct1').value = '';
    document.getElementById('ct2').value = '';
    document.getElementById('ct3').value = '';
    document.getElementById('ct4').value = '';
    document.getElementById('ct5').value = '';
    document.getElementById('ct6').value = '';
}
// Letra d
var b4 = document.getElementById('b4');
b4.addEventListener('click', clickb4);

function clickb4() {
    document.getElementById('ct6').value = document.getElementById('ct5').value;
}