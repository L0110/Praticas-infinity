/*
Crie uma aplicação simples de Organizador de Tarefas utilizando JavaScript para praticar a utilização de Eventos DOM e seus conceitos. O projeto deve permitir ao usuário adicionar, remover e marcar tarefas como concluídas através de métodos, seletores e manipulação de elementos. 

Requisitos do Projeto:

a) Estrutura HTML Inicial:
- Crie uma área onde o usuário possa inserir uma tarefa.
- Adicione um botão "Adicionar Tarefa" que, ao ser clicado, insira a tarefa na lista de tarefas.
- Exiba a lista de tarefas em uma lista (ordenada ou não ordenada).

b) Adicionando Tarefas:
- Ao clicar no botão "Adicionar Tarefa", o texto da tarefa inserido pelo usuário deve ser adicionado como um novo item na lista de tarefas.

c) Marcar Tarefas como Concluídas:
- Permita que o usuário marque uma tarefa como concluída ao clicar sobre ela.
- Utilize a propriedade classList para adicionar uma classe CSS à tarefa (por exemplo, .concluída). Isso pode alterar o estilo da tarefa (exemplo: riscar o texto).

d) Remover Tarefas:
- Adicione um botão "Remover" ao lado de cada tarefa, ou uma caixa de seleção que permita remover múltiplas tarefas.
- Ao clicar no botão "Remover", a tarefa deve ser removida da lista.
- Utilize o método removeChild() para remover o item da lista.

e) Eventos DOM:
- Use o método addEventListener() para detectar os eventos de clique para adicionar, remover e marcar as tarefas como concluídas.

*/
// Seletores presentes no index.html
const tarefaInput = document.getElementById("tarefaInput");
const adicionarBtn = document.getElementById("adicionarBtn");
const listaTarefas = document.getElementById("listaTarefas");
const removerBtn = document.getElementById('removerBtn');

// Função para adicionar tarefa
function adicionarTarefa() {
    const tarefaTexto = tarefaInput.value;
    if (tarefaTexto) {
        const li = document.createElement("li");

        // Botao de concluido
        const concluidoBtn = document.createElement("input");
        concluidoBtn.type = "checkbox";
        concluidoBtn.addEventListener("click", function(event) {
            event.stopPropagation();
            li.classList.toggle("concluida");
        });
        li.appendChild(concluidoBtn);

        // Exibição da tarefa
        const span = document.createElement("span");
        span.textContent = "\t[ " + tarefaTexto + " ]\t";
        li.appendChild(span);

        listaTarefas.appendChild(li);

        // Botao de apagar
        const removerBtn = document.createElement("button");
        removerBtn.textContent = "Remover";
        removerBtn.addEventListener("click", function(event) {
            event.stopPropagation();
            removerTarefa(event);
        });
        li.appendChild(removerBtn);
        tarefaInput.value = "";

    }
}

// Função para marcar tarefa como concluída
function marcarComoConcluida(event) {
    event.target.classList.toggle("concluida");
}

// Evento de clique para adicionar tarefa
adicionarBtn.addEventListener("click", adicionarTarefa);

// Função para remover tarefa
function removerTarefa(event) {
    const li = event.target.parentElement;
    listaTarefas.removeChild(li);
}

// Evento de clique para remover tarefa
removerBtn.addEventListener("click", removerTarefa);


