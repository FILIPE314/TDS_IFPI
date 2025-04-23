function getById(id) {
    return document.getElementById(id);
}

function clique(id, funcao) {
    getById(id).addEventListener('click', funcao);
}

clique('b1', () => {
    let i1 = parseInt(getById('ct1').value);
    let i2 = parseInt(getById('ct2').value);
    var som = i1 + i2;
    var sub = i1 - i2;
    let result = som + '<br>' + sub + '<br>' + i1 * i2 + '<br>' + i1 / i2;
    getById('p1').innerHTML = result
});