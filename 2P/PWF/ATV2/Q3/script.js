// letra a
var b1 = document.getElementById('b1');
b1.addEventListener('click', clickb1);

function clickb1() {
    var div = document.getElementById('paragrafo');
    let aleatorio = Math.floor(Math.random() * 10) + 1;
    div.innerHTML = parseInt(aleatorio);
}
// letra b
var b2 = document.getElementById('b2');
b2.addEventListener('click', clickb2);

function clickb2() {
    const ct1 = document.getElementById('ct1').value;
    const result = Math.abs(parseFloat(ct1));
    var pr = document.getElementById('paragrafo2');
    pr.innerHTML = result;
}
// letra c
var b3 = document.getElementById('b3');
b3.addEventListener('click', clickb3);

function clickb3() {
    const ct2 = document.getElementById('ct2').value;
    const ct3 = document.getElementById('ct3').value;
    const result = Math.max(ct2, ct3);
    var pr = document.getElementById('paragrafo3');
    pr.innerHTML = result;
}
// letra d
var b4 = document.getElementById('b4');
b4.addEventListener('click', clickb4);

function clickb4() {
    const ct4 = document.getElementById('ct4').value;
    const result = Math.round(parseFloat(ct4));
    var pr = document.getElementById('paragrafo4');
    pr.innerHTML = result;
}
// letra e
var b5 = document.getElementById('b5');
b5.addEventListener('click', clickb5);

function clickb5() {
    const ct5 = document.getElementById('ct5').value;
    const ct6 = document.getElementById('ct6').value;
    const result = Math.pow(ct5, ct6);
    var pr = document.getElementById('paragrafo5');
    pr.innerHTML = result;
}