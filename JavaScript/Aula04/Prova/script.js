/*
Crie um programa em JavaScript que permita ao usuário gerenciar uma lista de compras utilizando arrays. O programa deve permitir a adição de itens, a remoção de itens e a exibição de todos os itens da lista.

Requisitos do Projeto:
* Adicionar Itens:
 - Utilize o método push() para permitir que o usuário adicione novos itens à lista de compras.

* Remover Itens:
 - Permita que o usuário remova um item específico utilizando o método splice().
 - O programa deve solicitar o índice do item a ser removido.

* Exibir Lista:
 - Use um loop for...of para percorrer e exibir os itens da lista. Cada item deve ser mostrado com seu respectivo índice.

* Atualizar Itens:
 - Permita que o usuário atualize um item da lista ao fornecer o índice e o novo valor.
*/
let indice = 0;
let produto = null;
let valor = null;
let quantidade = null;
let listaCompras = [];
let op = 0;

let padrao01 = "➕".repeat(3);
let padrao02 = "➖".repeat(3);
let padrao03 = "❌".repeat(3);
let padrao04 = "👁️".repeat(3);

// Adicionar itens na lista de compras
function adicionarProduto() {
    console.log(`Cod: (${indice})`)
    produto = prompt(`Nome do produto:`);
    valor = prompt(`Valor do produto:`);
    quantidade = prompt(`Quantidade do produto:`);
    listaCompras.push({ indice, produto, valor, quantidade });
    indice++;
    console.log(listaCompras);
    return console.log("Produto adicionado ✅")
}
// listaCompras[{indice},{produto},{valor},{quantidade}]

// Remover um item da lista de compras
function removerProduto() {
    let seletor = null;
    seletor = parseInt(prompt("Informe o ID do produto: "));
    if (seletor != null) {
        listaCompras.splice(seletor, 1);
        for (let i = 0; i < listaCompras.length; i++) {
            listaCompras[i].indice = i;
            if (listaCompras.length>0){
                indice = i+1;
            }
        }
        return console.log("produto removido 🧹");
        
    }else{
        return console.log("erro ao remover ❌");
    }
}
// Exibicao da lista de compras indicando seu numero do indice(for... of)
function visualizarLista() {
    let html = "";
    for (let i = 0; i < listaCompras.length; i++) {
        html += `<li>(${listaCompras[i].indice}) | Produto: ${listaCompras[i].produto} | R$ ${listaCompras[i].valor} | ${listaCompras[i].quantidade} Unidades</li>`;
    }
    let lis = document.getElementById("listagem");
    lis.innerHTML = html;
}

// Atualizar um item da lista ao fornecer o indice e o novo valor
function alterarProduto() {
    let seletor = prompt("Informe o ID do produto: ");
    listaCompras[seletor].valor = prompt("Informe o novo valor: ");
    listaCompras[seletor].quantidade = prompt("Informe a nova Quantidade: ");
    return console.log("produto alterado 🧹");
}

let tit = document.getElementById("titulo");
// [menu]
function menu() {
    op = prompt("1- Adicionar produto a lista\n2- Alterar lista\n3- Exluir produto a lista\n4- Visualizar a lista\nDigite aqui: ");
    let opcao = parseInt(op);
    switch (opcao) {
        case 1:
            console.log(`${padrao01} Adicionar produto a lista ${padrao01}`);
            adicionarProduto();
            break;
        case 2:
            console.log(`${padrao02} Alterar lista ${padrao02}`);
            alterarProduto();
            break;
        case 3:
            console.log(`${padrao03} Exluir produto a lista ${padrao03}`);
            removerProduto();
            break;
        case 4:
            console.log(`${padrao04} Visualizar a lista ${padrao04}`);
            tit.innerHTML = `${padrao04} Visualizar a lista ${padrao04}`;
            visualizarLista();
            break;
        default:
            alert("Escolha uma opcao valida")
    }
}
