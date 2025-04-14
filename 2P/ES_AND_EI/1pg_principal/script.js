function getByid(id) {
    return document.getElementById(id);
}

var b1 = getByid('b1');
var t1 = getByid('t1');
var b2 = getByid('b2');
var ct1 = getByid('ct1');
b1.addEventListener('click', () => {
    b1.classList.add('botaosair');
    b2.classList.add('b2entrar');
    ct1.classList.add('ct1entrar');
});



function perguntaNome() {
    const ct1 = document.getElementById('ct1');
    const mensagemElement = document.getElementById('mensagem');
    
    if (ct1.value.trim() === '') {
        mensagemElement.textContent = 'Por favor, digite seu nome.';
        mensagemElement.style.color = 'red';

    } else {
        mensagemElement.textContent = `Olá, ${ct1.value}! Bem-vindo(a).`;
        mensagemElement.style.color = 'green';
        
        t1.classList.add('titulosair');
        b2.classList.add('b2sair');
        ct1.classList.add('ct1sair');
        
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
