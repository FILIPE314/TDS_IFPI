// Letra a
var b1 = document.getElementById('b1');
b1.addEventListener('click', clickb1);

function clickb1() {
    let txt = document.getElementById('texto');
    var p1 = document.getElementById('p1');
    let len = txt.textContent.length;
    p1.innerHTML = len;
}
// Letra b
var b2 = document.getElementById('b2');
b2.addEventListener('click', clickb2);

function clickb2() {
    let txt = document.getElementById('texto');
    let min = txt.textContent.toLowerCase();
    var p2 = document.getElementById('p2');
    p2.innerHTML = min;
}
// Letra c
var b3 = document.getElementById('b3');
b3.addEventListener('click', clickb3);

function clickb3() {
    let txt = document.getElementById('texto');
    let recolocado = txt.textContent.replace(/A/ig, '@').replace(/E/ig, '3').replace(/I/ig, '1').replace(/O/ig, '0');    
    var p3 = document.getElementById('p3');
    p3.innerHTML = recolocado;
}
// Letra d
var b4 = document.getElementById('b4');
b4.addEventListener('click', clickb4);

function clickb4() {
    let txt = document.getElementById('texto');
    let space = txt.textContent;
    var p4 = document.getElementById('p4');
    p4.innerHTML = space;
}