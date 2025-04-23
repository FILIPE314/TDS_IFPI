let pontuacao = parseInt(localStorage.getItem('pontuacao')) || 0;

function verificarResposta(selectedButton) {
    const buttons = document.querySelectorAll('.resposta');
    buttons.forEach(button => {
        button.disabled = true;
        button.style.opacity = '0.5';
    });

    const resultDiv = document.getElementById('resultado');
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const mensagem = document.getElementById('mensagem');
    const proximoBotao = document.getElementById('proximoBotao');
    const tentarNovamenteBotao = document.getElementById('tentarNovamenteBotao');

    if (selectedButton.getAttribute('resposta-correta') === 'true') {
        pontuacao += 3;
        localStorage.setItem('pontuacao', pontuacao);
        document.getElementById('pontuacao').textContent = `Pontuação: ${pontuacao}`;

        mensagem.textContent = 'Resposta correta!';
        mensagem.style.color = 'green';
        proximoBotao.style.display = 'inline-block';
        tentarNovamenteBotao.style.display = 'none';
    } else {
        mensagem.textContent = 'Resposta incorreta!';
        mensagem.style.color = 'red';
        proximoBotao.style.display = 'none';
        tentarNovamenteBotao.style.display = 'inline-block';
    }

    popup.style.display = 'block';
    overlay.style.display = 'block';
}

function proximaFase() {
    let currentPage = window.location.href.split('/').pop();
    let phaseNumber = parseInt(currentPage.match(/\d+/)[0]);

    if (phaseNumber < 12) {
        phaseNumber++;
        window.location.href = `pergunta${phaseNumber}.html`;
    } else {
        alert("Você completou todas as fases!");
        setTimeout(() => {
            window.location.href = '/5pg_final/index.html';
            }, 3000);
    }

    fecharPopup();
}

function tentarNovamente() {
    location.reload();
}

function fecharPopup() {
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function () {
    const pontuacaoSalva = localStorage.getItem('pontuacao');
    if (pontuacaoSalva) {
        document.getElementById('pontuacao').textContent = `Pontuação: ${pontuacaoSalva}`;
    }
});
