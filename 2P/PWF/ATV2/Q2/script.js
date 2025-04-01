var ct = document.getElementById('ct')
var b1 = document.getElementById('b1');
b1.addEventListener('click', clickb1);

function clickb1() {
    var div = document.getElementById('paragrafo');
    div.innerHTML = 'Boa tarde, ' + ct.value + '<br>';
}

var b2 = document.getElementById('b2');
b2.addEventListener('click', clickb2);

function clickb2() {
    var div = document.getElementById('paragrafo');
    div.innerHTML = div.innerHTML + 'Boa noite, ' + ct.value + '<br>';
}