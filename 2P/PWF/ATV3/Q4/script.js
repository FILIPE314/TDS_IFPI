function getById(id) {
    return document.getElementById(id);
}

function click(id, funcao) {
    getById(id).addEventListener('click', funcao);
}

click('b1', () => {
    const d = new Date();
    const d2 = d.getDay() + 10;
    const d3 = d.getMonth() + 1;
    const d4 = d.getFullYear();
    getById('p1').innerHTML = d2 + '/' + d3 + '/' + d4;
})