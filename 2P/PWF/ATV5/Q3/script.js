function getById(id) {
    return document.getElementById(id);
};

var b1 = getById('b1');
b1.addEventListener('click', () => {
    var hora1 = getById('hora').value;
    if (hora1 >= 18) {
        var corpo = getById('corpo');
        corpo.style.background = 'black';
        corpo.style.color = 'white';
    };
    if (hora1 <= 6) {
        var corpo = getById('corpo');
        corpo.style.background = 'black';
        corpo.style.color = 'white';
    }
});