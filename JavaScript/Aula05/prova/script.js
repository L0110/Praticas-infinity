/*

Crie um programa em que permita ao usuário gerenciar uma lista de tarefas usando arrays e loops. O programa deve oferecer as opções de adicionar, remover, listar e concluir tarefas, enquanto manipula o array de tarefas e utiliza loops para percorrê-lo.

Requisitos do Projeto:
* Adicionar Tarefas:
- Solicite ao usuário o nome de uma tarefa e adicione-a ao final do array usando o método push().

* Listar Tarefas:
- Use um loop for ou for...of para percorrer o array de tarefas e exibi-las com seus índices.

* Remover Tarefas:
- Solicite ao usuário o índice da tarefa que deseja remover e utilize o método splice() para removê-la do array.


* Concluir Tarefas (Opcional):
- Peça ao usuário o índice de uma tarefa e marque-a como concluída, modificando a string para algo como "✅ Lavar a louça".

* Interação Contínua:
- Utilize um loop while para continuar solicitando ações do usuário (adicionar, listar, remover, concluir) até que ele escolha sair.

*/

// * Adicionar Tarefas:
let tarefas = [];
let id = 0;
let tarefa = null;
let status = null;
let op = null;

//avisos
const avisoCadastroSucesso = (tarefa) => `[Tarefa adicionada com sucesso!]: "${tarefa}"`;
const avisoOpInvalida = "Informe uma opção válida";
const opMenu = "1 - Adicionar tarefa\n2 - Listar tarefa\n3 - Remover tarefa\n4 - Concluir tarefa\n0 - Sair\n[digite uma opção]:";


function adicionarTarefa() {
    let tarefa = prompt("[Nova tarefa]:");
    let status = "❌";
    tarefas.push({ id, tarefa, status });
    id++;
    console.log(avisoCadastroSucesso(tarefa));
    alert(avisoCadastroSucesso(tarefa));
}
// * Listar Tarefas:
function listarTarefas() {
    if (tarefas.length === 0) {
        console.log("Nenhuma tarefa cadastrada!");
        return;
    }
    console.log("\nLista de Tarefas:");
    for (let item of tarefas) {
        console.log(`[${item.id}] ${item.tarefa} ${item.status}`);
    }
}
// * Remover Tarefas:
function removerTarefa() {
    let seletor = null;
    seletor = parseInt(prompt("[Informe o ID da tarefa]: "));
    if (seletor != null) {
        tarefas.splice(seletor, 1);
        for (let i = 0; i < tarefas.length; i++) {
            tarefas[i].id = i;
            if (tarefas.length > 0) {
                id = i + 1;
            }
        }
        return console.log("Tarefa removida 🧹");

    } else {
        return console.log("erro ao remover ❌");
    }
}
// * Concluir Tarefas (Opcional):
function alterarStatus() {
    let seletor = null;
    seletor = parseInt(prompt("[Informe o ID da tarefa]: "));
    if (seletor != null && seletor < tarefas.length) {
        tarefas[seletor].status = "✅";
        console.log(`Tarefa concluída: "${tarefas[seletor].tarefa}"`);
        alert(`Tarefa concluída: "${tarefas[seletor].tarefa}"`);
    } else {
        console.log("ID inválido ❌");
        alert("ID inválido ❌");
    }
}
// * Interação Contínua:

function opcoes() {
    console.log(opMenu);
    op = parseInt(prompt(opMenu));
}
function menu() {
    switch (op) {
        case 0:
            console.log("Programa finalizado!");
            return false;
        case 1:
            adicionarTarefa();
            break;
        case 2:
            listarTarefas();
            break;
        case 3:
            removerTarefa();
            break;
        case 4:
            alterarStatus();
            break;
        default:
            alert(avisoOpInvalida);
    }
    return true;
}

let continuar = true;
while (continuar) {
    opcoes();
    continuar = menu();
} opcoes();
menu();