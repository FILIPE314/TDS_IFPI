function getByid(id) {
    return document.getElementById(id);
}

var b1 = getByid('b1');
var t1 = getByid('t1');
var b2 = getByid('b2');
var ct1 = getByid('ct1');
var sup = getByid('sup');
b1.addEventListener('click', () => {
    b1.classList.add('botaosair');
    b2.classList.add('b2entrar');
    ct1.classList.add('ct1entrar');
});



function perguntaNome() {
    const ct1 = document.getElementById('ct1');
    const mensagemElement = document.getElementById('mensagem');

    localStorage.setItem('playerName', ct1.value);
    
    if (ct1.value.trim() === '') {
        mensagemElement.textContent = 'Por favor, digite seu nome.';
        mensagemElement.style.color = 'red';

    } else {
        mensagemElement.textContent = `Seja Bem-vindo ${ct1.value}`;
        mensagemElement.style.color = 'lightgreen';
        localStorage.setItem('playerName', ct1.value);
        
        t1.classList.add('titulosair');
        b2.classList.add('b2sair');
        ct1.classList.add('ct1sair');
        sup.classList.add('titulosair');
        
        setTimeout(() => {
            window.location.href = '../2pg_personagens/index.html';
        }, 3000);
    }
}


document.getElementById('ct1').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        perguntaNome();
    }
});

localStorage