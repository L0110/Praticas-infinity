let i = 0;

function salvar(){
    i++;
    let novaTarefa = document.getElementById("tarefa").value;
    
    const vlrH3 = document.getElementsByTagName("h3")[0];
    vlrH3.innerHTML += `${i} - ${novaTarefa}<br/>`;
    
    localStorage.setItem(i, novaTarefa);
}

function remover(){
    if (i > 0) {
        localStorage.removeItem(i);
        i--;
        // Atualiza a exibição das tarefas
        atualizarExibicao();
    }
}

function apagar(){
    localStorage.clear();
    i = 0;
    // Limpa a exibição das tarefas
    document.getElementsByTagName("h3")[0].innerHTML = "";
}

function atualizarExibicao() {
    const vlrH3 = document.getElementsByTagName("h3")[0];
    vlrH3.innerHTML = "";
    for (let j = 1; j <= i; j++) {
        const tarefa = localStorage.getItem(j);
        if (tarefa) {
            vlrH3.innerHTML += `${j} - ${tarefa}<br/>`;
        }
    }
}
