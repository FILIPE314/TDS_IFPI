document.getElementById('dogForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const count = document.getElementById('dogCount').value;
    fetch(`https://api.thedogapi.com/v1/images/search?limit=${count}`)
        .then(response => response.json())
        .then(data => {
            const gallery = document.getElementById('dogGallery');
            gallery.innerHTML = '';
            data.forEach(dog => {
                const img = document.createElement('img');
                img.src = dog.url;
                gallery.appendChild(img);
            });
        })
        .catch(error => console.error('Erro ao carregar imagens de cães:', error));
});

document.getElementById('catForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const count = document.getElementById('catCount').value;
    fetch(`https://catfact.ninja/facts?limit=${count}`)
        .then(response => response.json())
        .then(data => {
            const factsDiv = document.getElementById('catFacts');
            factsDiv.innerHTML = '';
            const promises = data.data.map(fact => translateToPortuguese(fact.fact));
            Promise.all(promises).then(translatedFacts => {
                translatedFacts.forEach(translatedFact => {
                    const p = document.createElement('p');
                    p.className = 'fact';
                    p.textContent = translatedFact;
                    factsDiv.appendChild(p);
                });
            });
        })
        .catch(error => console.error('Erro ao carregar fatos sobre gatos:', error));
});

async function translateToPortuguese(text) {
    const response = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=en|pt`);
    const data = await response.json();
    return data.responseData.translatedText || text;
}