let i = 0;

function salvar(){
    i++;
    let novaTarefa = document.getElementById("tarefa").value;
    localStorage.setItem(i,"tarefa");
    
    const vlrH3 = document.getElementsByTagName("h3")[0];
    vlrH3.innerHTML += `${i+1} - ${novaTarefa}<br/>`;
    
    localStorage.setItem(i,novaTarefa)
}

function remover(){
    localStorage.removeItem(i);
    i--;
}

function apagar(){
    localStorage.clear();
}