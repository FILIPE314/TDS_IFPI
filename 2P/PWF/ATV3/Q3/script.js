function getById(id) {
    return document.getElementById(id);
}

function click(id, funcao) {
    getById(id).addEventListener('click', funcao);
}

click('b1', () => {
    let i1 = parseInt(getById('ct1').value);
    var result = i1 * 1.8;
    getById('p1').innerHTML = result + 32;
});