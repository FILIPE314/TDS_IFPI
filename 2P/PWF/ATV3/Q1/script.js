function getById(id) {
    return document.getElementById(id);
}

function clique(id, funcao) {
    getById(id).addEventListener('click', funcao); 
}

clique('b1', () => {
    let text = getById('ct1').value;
    p1 = getById('p1');
    p1.innerHTML = text.padStart(5, "0");
});