function getByID(id) {
    return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');
botaoConsultar.addEventListener('click', consultarPreco);
async function consultarPreco() {

    const box1 = document.getElementById('moedaBase');
    const box2 = document.getElementById('moedaConversao');
    
    if (box1.value.trim() === "" || box2.value.trim() === "") {
        alert("Uma ou ambas as caixas de texto estão vazias!");
    }

    let moedaBase = getByID('moedaBase').value.toUpperCase(); // Moeda base (ex.: BTC)
    let moedaConversao = getByID('moedaConversao').value.toUpperCase(); // Moeda de conversão (ex.: USDT)
    let resultado = getByID('resultado');
    let url = `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;
    try {
        let response = await fetch(url); // Faz a requisição à API Binance
    if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
    }
    let json = await response.json();

    resultado.innerHTML = `
        <p><strong>Par de Moedas:</strong> ${json.symbol}</p>
        <p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)
    }

    ${moedaConversao}</p>`;
        } catch (error) {
            resultado.innerHTML = 'Erro: ' + error.message;
        }
}

var b1 = document.getElementById('b1');
b1.addEventListener('click', clickb1);

function clickb1() {
    document.getElementById('moedaBase').value = '';
    document.getElementById('moedaConversao').value = '';
    resultado.innerHTML = '';
}

var b1 = document.getElementById('b2');
b2.addEventListener('click', clickb2);

function clickb2() {
    // Seleciona as caixas de texto
    const box1 = document.getElementById('moedaBase');
    const box2 = document.getElementById('moedaConversao');
    
    // Troca os valores
    const temp = box1.value;
    box1.value = box2.value;
    box2.value = temp;
}

