function getByid(id) {
    return document.getElementById(id);
}

const levels = [
    { id: 1, name: 'Fase1' },
    { id: 2, name: 'Fase2' },
    { id: 3, name: 'Fase3' },
    { id: 4, name: 'Fase4' },
    { id: 5, name: 'Fase5' },
    { id: 6, name: 'Fase6' },
    { id: 7, name: 'Fase7' },
    { id: 8, name: 'Fase8' },
    { id: 9, name: 'Fase9' },
    { id: 10, name: 'Fase10' },
    { id: 11, name: 'Fase11' },
    { id: 12, name: 'Fase12' }
];

let selectedCharacter = null;

const Cards = document.querySelectorAll('.level');

Cards.forEach(card => {
    card.addEventListener('click', () => {
        Cards.forEach(c => c.classList.remove('selected'));

        card.classList.add('selected');

        selectedCharacter = levels.find(level => 
            level.id === parseInt(card.dataset.id)
        );

        console.log(`Fase selecionada: ${selectedCharacter ? selectedCharacter.name : 'Nenhuma'}`);
    });
});

const b1 = getByid('b1');
b1.addEventListener('click', seleciona);

function seleciona() {
    if (selectedCharacter) {
        console.log(`Redirecionando para pergunta ${selectedCharacter.id}...`);

        setTimeout(() => {
            window.location.href = `../4pg_perguntas/Perguntas/pergunta${selectedCharacter.id}.html`;
        }, 1);
    } else {
        alert("Nenhuma fase foi selecionada!");
    }
}