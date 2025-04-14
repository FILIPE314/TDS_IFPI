const characters = [
    {
        id: 1,
        name: 'Bastião',
    },    
];

const characterCards = document.querySelectorAll('.character-card');
const confirmationDiv = document.getElementById('confirmation');
const confirmButton = document.getElementById('confirm-button');
const confirmationMessage = document.getElementById('confirmation-message');
const selectedCharacterName = document.getElementById('selected-character-name');

let selectedCharacter = null;

characterCards.forEach(card => {
    card.addEventListener('click', () => {
        characterCards.forEach(c => c.classList.remove('selected'));
        
        card.classList.add('selected');
        
        confirmationDiv.classList.remove('hidden');
        
        selectedCharacter = characters.find(char => 
            char.id === parseInt(card.dataset.id)
        );
        
        confirmationMessage.classList.add('hidden');
    });
});

confirmButton.addEventListener('click', () => {
    if (selectedCharacter) {
        confirmationMessage.classList.remove('hidden');
        selectedCharacterName.textContent = selectedCharacter.name;
        
        confirmationDiv.classList.add('hidden');
    }

        setTimeout(() => {
        window.location.href = '../3pg_fases/index.html';
        }, 3000);
});