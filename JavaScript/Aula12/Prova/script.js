/*
a) Interface HTML Inicial:
- Crie um campo de texto para o título da nota.
- Adicione um botão para adicionar nota.
- Crie uma lista para exibir as notas armazenadas.

b) Adição de Notas:
- Ao clicar no botão "Adicionar Nota":
- Leia o valor do campo de texto (título da nota).
- Armazene a nota como um objeto no Local Storage. Cada nota deve ter um título único.
- Atualize a lista de notas exibida na tela, mostrando o título e um botão "Remover".

c) Listar Notas:
- Utilize o Local Storage para recuperar as notas armazenadas.
- Transforme os dados recuperados de volta para objetos.
- Exiba as notas em uma lista, mostrando o título de cada nota e um botão "Remover" ao lado de cada uma.

d) Remover Notas:
- Ao clicar no botão "Remover", a nota correspondente do Local Storage.
- Atualize a lista de notas exibida na tela, removendo a nota excluída.

e) Armazenamento no Local Storage:
- Salve as notas no Local Storage.
- Carregue as notas.
- Armazene objetos como strings no Local Storage.
- Recupere os dados do Local Storage e transforme os de volta em objetos JavaScript.
*/

let i = 0;
const listaTarefas = document.getElementById("listaTarefas");
const tarefaInput = document.getElementById("tarefa");

function concluirTarefa(element) {
    const li = element.parentElement;
    li.classList.toggle("concluida");
}

function criarItemLista(texto, concluida, idx) {
    const li = document.createElement("li");
    li.textContent = texto;
    if (concluida) {
        li.classList.add("concluida");
        li.onclick = () => desfazerTarefa(idx);
    } else {
        li.onclick = () => concluirTarefa(idx);
    }

    // Botão remover
    const btnRemover = document.createElement("span");
    btnRemover.textContent = " ❌";
    btnRemover.style.cursor = "pointer";
    btnRemover.onclick = (e) => {
        /* Não dispara o evento de riscar/mover */
        e.stopPropagation();
        removerTarefa(idx);
    };
    li.appendChild(btnRemover);

    return li;
}

function atualizarExibicao() {
    const tarefas = getTarefas();
    listaTarefas.innerHTML = "";
    listaConcluidas.innerHTML = "";
    tarefas.forEach((tarefa, idx) => {
        const li = criarItemLista(`${idx + 1} - ${tarefa.texto}`, tarefa.concluida, idx);
        if (tarefa.concluida) {
            listaConcluidas.appendChild(li);
        } else {
            listaTarefas.appendChild(li);
        }
    });
}

// Salvar todas as tarefas no local storage
function setTarefas(tarefas) {
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

// Recuperar todas as tarefas do local storage
function getTarefas() {
    return JSON.parse(localStorage.getItem("tarefas") || "[]");
}

// Adicionar nova tarefa 
function salvar(event) {
    event.preventDefault();
    const texto = tarefaInput.value.trim();
    if (!texto) return;
    const tarefas = getTarefas();
    tarefas.push({ texto, concluida: false });
    setTarefas(tarefas);
    tarefaInput.value = "";
    atualizarExibicao();
}

// Desfazer tarefa pelo índice
function concluirTarefa(idx) {
    const tarefas = getTarefas();
    tarefas[idx].concluida = true;
    setTarefas(tarefas);
    atualizarExibicao();
}
function desfazerTarefa(idx) {
    const tarefas = getTarefas();
    tarefas[idx].concluida = false;
    setTarefas(tarefas);
    atualizarExibicao();
}

// Remover tarefa pelo índice
function removerTarefa(idx) {
    const tarefas = getTarefas();
    tarefas.splice(idx, 1);
    setTarefas(tarefas);
    atualizarExibicao();
}
function apagar(event) {
    event.preventDefault();
    localStorage.removeItem("tarefas");
    atualizarExibicao();
}

// Inicialização
atualizarExibicao();
