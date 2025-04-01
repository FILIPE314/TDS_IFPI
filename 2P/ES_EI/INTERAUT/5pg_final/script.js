// Pega os dados armazenados no localStorage
const playerName = localStorage.getItem("playerName") || "Jogador";
const playerScore = localStorage.getItem("playerScore") || 0;

// Exibe os dados na página final
document.getElementById("playerName").textContent = playerName;
document.getElementById("score").textContent = playerScore;