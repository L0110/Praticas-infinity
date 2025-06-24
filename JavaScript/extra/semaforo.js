let nodeListLuzes = document.querySelectorAll(".luz");
const botao = document.getElementById("proxima-cor");
let indice = 0;

// Funcao para alternar as luzes do semáforo
function trocarLuz(){
    // Apagar todas as luzes:
    nodeListLuzes.forEach(luz => luz.classList.remove("on"));
    // Acender a luz atual:
    nodeListLuzes[indice].classList.add("on");
    // Avançar o índice para a próxima cor, reiniciar para 0 {1,2,0,...}:
    indice = (indice + 1) % nodeListLuzes.length;
    setTimeout(trocarLuz,2000); // Chamar a função novamente após 2 segundos
    // Atualizar o texto do botão:

}

trocarLuz(); // Acender a luz vermelha

// botao.addEventListener("click", trocarLuz); // Adicionar o evento de clique no botão