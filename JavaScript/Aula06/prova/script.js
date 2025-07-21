/*
Crie um programa que utiliza funções anônimas, arrow functions e funções de callback para gerenciar e processar uma lista de tarefas.
Requisitos do Projeto:
* Criação de Funções Anônimas:
 - Use uma função anônima para adicionar tarefas a uma lista. A função deve ser atribuída a uma variável e permitir adicionar uma nova tarefa ao array de tarefas.

* Uso de Arrow Functions:
 - Implemente uma arrow function para listar todas as tarefas, exibindo cada tarefa com seu índice no console.

* Funções de Callback:
 - Crie uma função que receba outra função como callback. Essa função deve permitir executar diferentes operações com a lista de tarefas, como:
 - Remover uma tarefa.
 - Atualizar uma tarefa.
 - Concluir uma tarefa.

* Interação com o Usuário:
 - Utilize métodos como prompt() para receber ações do usuário e exiba os resultados no console usando console.log(). 
 */

let tarefas = [];
let id = 0;
let op = null;

const avisoOpInvalida = "Informe uma opção válida";
const opMenu = ["1 - Adicionar tarefa\n","2 - Listar tarefa\n","3 - Remover tarefa\n","4 - Concluir tarefa\n","0 - Sair\n"];

const msgStatus = status => status === false ? "Tarefa em aberto" : "Tarefa concluída";
const msgRemoverTarefa = seletor => seletor != null ? "Tarefa removida" : "Erro ao remover";

let novaTarefa = function(){
    let tarefaDesc = prompt("[Nova tarefa]: ");
    tarefas.push({id, tarefa: tarefaDesc, status: false});
    id++;
    console.log(`[Tarefa adicionada com sucesso!]: "${tarefaDesc}"`);
};

let removerTarefa = function(){
    let seletor = parseInt(prompt("[Informe o ID da tarefa]: "));
    if (!isNaN(seletor) && seletor >= 0 && seletor < tarefas.length) {
        tarefas.splice(seletor, 1);
        // Renumerar ids
        for (let i = 0; i < tarefas.length; i++) {
            tarefas[i].id = i;
        }
        id = tarefas.length;
        console.log("Tarefa removida");
    } else {
        console.log("Erro ao remover");
    }
};

let alterarTarefa = function(){
    let seletor = parseInt(prompt("[Informe o ID da tarefa para atualizar]: "));
    if (!isNaN(seletor) && seletor >= 0 && seletor < tarefas.length) {
        let novaDesc = prompt("Nova descrição para a tarefa: ");
        tarefas[seletor].tarefa = novaDesc;
        console.log("Tarefa atualizada");
    } else {
        console.log("ID inválido");
    }
};

let concluirTarefa = function(){
    let seletor = parseInt(prompt("[Informe o ID da tarefa para concluir]: "));
    if (!isNaN(seletor) && seletor >= 0 && seletor < tarefas.length) {
        tarefas[seletor].status = true;
        console.log(`Tarefa concluída: "${tarefas[seletor].tarefa}"`);
    } else {
        console.log("ID inválido");
    }
};

let listarTarefas = () => {
    if (tarefas.length === 0) {
        console.log("Nenhuma tarefa cadastrada!");
        return;
    }
    console.log("\nLista de Tarefas:");
    for (let item of tarefas) {
        console.log(`[${item.id}] ${item.tarefa} | ${msgStatus(item.status)}`);
    }
};

let opcoes = function() {
    op = parseInt(prompt(`${opMenu.join(" ")}[digite uma opção]: `));
};

let menu = function() {
    switch (op) {
        case 0:
            console.log("Programa finalizado!");
            return false;
        case 1:
            novaTarefa();
            break;
        case 2:
            listarTarefas();
            break;
        case 3:
            removerTarefa();
            break;
        case 4:
            concluirTarefa();
            break;
        case 5:
            alterarTarefa();
            break;
        default:
            alert(avisoOpInvalida);
    }
    return true;
};

let continuar = true;
while (continuar) {
    opcoes();
    continuar = menu();
}