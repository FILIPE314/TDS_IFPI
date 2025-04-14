function getById(id) {
    return document.getElementById(id);
}

var botao = getById('alterar');
botao.addEventListener('click', () => {
    var caixa1 = getById('caixa');
    caixa1.style.visibility = 'hidden';
});

var botao2 = getById('alterar2');
botao2.addEventListener('click', () => {
    var caixa1 = getById('caixa');
    caixa1.style.visibility = 'visible';
});

// ==============================================

var bot1 = getById('b1');
var bot2 = getById('b2');
bot1.addEventListener('click', () => {
    var texto = getById('text')
    texto.style.fontSize = 16 + 'px'
});
bot2.addEventListener('click', () => {
    var texto = getById('text')
    texto.style.fontSize = 10 + 'px'
});

// ==============================================

