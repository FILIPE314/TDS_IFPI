function getByid(id) {
    return document.getElementById(id);
};

var b1 = getByid('alterarClasse');
b1.addEventListener('click', () => {
    var div = getByid('caixaClasse');
    div.classList.toggle('novoEstilo');
});