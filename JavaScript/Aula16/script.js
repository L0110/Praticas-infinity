// Função para atualizar a exibição usando o template do HTML
function atualizarExibicao() {

    const tarefas = getTarefas();
    // Limpa as colunas
    colunaPendentes.querySelectorAll('.card-tarefa.card-pendente').forEach(e => e.remove());
    colunaConcluidas.querySelectorAll('.card-tarefa.card-concluida').forEach(e => e.remove());

    // Seleciona o template
    const template = document.querySelector('template');
    const cardPendente = template.content.querySelector('.card-pendente');
    const cardConcluida = template.content.querySelector('.card-concluida');
    
    tarefas.forEach((tarefa, idx) => {
        let card;
        if (tarefa.concluida) {
            card = cardConcluida.cloneNode(true);
            // Preenche o texto
            card.querySelector('span.concluida').textContent = `${idx + 1} - ${tarefa.texto}`;
            // Botão desfazer
            card.querySelector('button:not(.btn-delete)').onclick = () => {
                const t = new Tarefa(tarefa.texto);
                t.id = tarefa.id;
                t.desfazerTarefa();
            };
        } else {
            card = cardPendente.cloneNode(true);
            // Preenche o texto
            card.querySelector('span').textContent = `${idx + 1} - ${tarefa.texto}`;
            // Botão concluir
            card.querySelector('button:not(.btn-delete)').onclick = () => {
                const t = new Tarefa(tarefa.texto);
                t.id = tarefa.id;
                t.concluirTarefa();
            };
        }
        // Botão remover (Para ambos)
        card.querySelector('.btn-delete').onclick = () => {
            const t = new Tarefa(tarefa.texto);
            t.id = tarefa.id;
            t.removerTarefa();
        };
        // Adiciona na coluna correta
        if (tarefa.concluida) {
            colunaConcluidas.appendChild(card);
        } else {
            colunaPendentes.appendChild(card);
        }
    });
}
let i = 0;
const btnAdd = document.getElementById("btn-add");
const btnClear = document.getElementById("btn-clear");
const btnBuscar = document.getElementById("btn-buscar"); // Adiciona esta linha para definir btnBuscar

// Seletores das colunas onde os cards serão inseridos

const colunaPendentes = document.querySelector('.coluna-01');
const colunaConcluidas = document.querySelector('.coluna-02');
const tarefaInput = document.getElementById("in-Tarefa");

class Tarefa{
    constructor(texto) {
        this.id = i++;
        this.texto = texto;
        this.concluida = false;
    }
    adicionar() {
        const tarefas = getTarefas();
        tarefas.push(this);
        setTarefas(tarefas);
        atualizarExibicao();
        tarefaInput.value = "";
        tarefaInput.focus();
        btnAdd.disabled = true;
    }
    removerTarefa() {
        const tarefas = getTarefas().filter((tarefa) => tarefa.id !== this.id);
        setTarefas(tarefas);
        atualizarExibicao();
    }
    concluirTarefa() {
        const tarefas = getTarefas();
        const tarefa = tarefas.find((tarefa) => tarefa.id === this.id);
        if (tarefa) {
            tarefa.concluida = true;
            setTarefas(tarefas);
            atualizarExibicao();
        }
    }
    desfazerTarefa() {
        const tarefas = getTarefas();
        const tarefa = tarefas.find((tarefa) => tarefa.id === this.id);
        if (tarefa) {
            tarefa.concluida = false;
            setTarefas(tarefas);
            atualizarExibicao();
        }
    }
}

// Adiciona listeners corretos aos botões
btnAdd.addEventListener("click", () => {
    const texto = tarefaInput.value.trim();
    if (texto) {
        const tarefa = new Tarefa(texto);
        tarefa.adicionar();
    }
});

btnBuscar.addEventListener("click", () => {
    const getApio = fetch("https://jsonplaceholder.typicode.com/todos").then(response => response.json());
    getApio.then(data => {
        data.forEach(item => {
            const tarefa = new Tarefa(item.title);
            tarefa.id = item.id;
            tarefa.concluida = item.completed;
            setTarefas(getTarefas().concat(tarefa));
        });
        atualizarExibicao();
    });
});

btnClear.addEventListener("click", () => {
    setTarefas([]);
    atualizarExibicao();
});

try{
    i = JSON.parse(localStorage.getItem("tarefas") || "[]").length;
    tarefaInput.addEventListener("input", () => {
        btnAdd.disabled = tarefaInput.value.trim() === "";
    });
}catch{
    localStorage.setItem("tarefas", "[]");
    i = 0;
    btnAdd.disabled = true;
    tarefaInput.addEventListener("input", () => {
        btnAdd.disabled = tarefaInput.value.trim() === "";
    });
    tarefaInput.value = "";
    tarefaInput.focus();
}

function getTarefas() {
    return JSON.parse(localStorage.getItem("tarefas") || "[]");
}

function setTarefas(tarefas) {
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
}


