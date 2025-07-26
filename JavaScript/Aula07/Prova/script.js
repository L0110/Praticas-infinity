/*
[JSIA-A07]  Crie um programa em JavaScript que gerencie uma lista de nomes utilizando diversos métodos auxiliares de arrays para realizar operações como adicionar, filtrar, encontrar e transformar os dados.

Requisitos do Projeto:
* Adicionar Nomes:✅
 - Permita ao usuário adicionar nomes à lista utilizando o método push().
 - Exiba a lista atualizada no console.

* Filtrar Nomes:✅
- Use o método filter() para criar uma nova lista contendo apenas os nomes que começam com uma letra específica fornecida pelo usuário.
 - Exiba os nomes filtrados no console.

* Buscar um Nome Específico:✅
- Use o método find() para localizar o primeiro nome na lista que corresponde exatamente a um valor fornecido pelo usuário.
 - Exiba o resultado no console ou uma mensagem informando que o nome não foi encontrado.

* Transformar Nomes:✅
- Utilize o método map() para transformar todos os nomes da lista em letras maiúsculas.
 - Exiba a nova lista no console.

* Verificar Condições:✅
 - Use o método every() para verificar se todos os nomes têm mais de três caracteres.
 - Exiba a resposta (true ou false) no console.

* Interação Contínua: ✅
 - Implemente um loop while para permitir que o usuário escolha realizar várias operações consecutivas (adicionar, filtrar, buscar, transformar ou verificar). 
 */
let op = null;
let letra = null;

// INCLUSAO DE NOMES
// let nomes = [];
let nomes = ["Ana", "Arlinda", "Bruno", "Carlos", "Diana", "Eduardo"];
let nome;
let adicionarNome = function(){
    nome = prompt("Informe um nome:");
    nomes.push(nome);
    console.log(`${nome} foi adicionado(a) a lista.`);
    console.log("Lista de nomes:");
    for (let i = 0; i < nomes.length; i++) {
        console.log(`${i + 1}: ${nomes[i]}`);
    }
}
// LOCALIZAR NOMES PELA LETRA INICIAL
let filtrarNomesLetra = function(){
    let letra = prompt("Digite uma letra para filtrar os nomes:");
    let nomesFiltrados = nomes.filter(nome => nome.startsWith(letra));
    if (nomesFiltrados.length > 0){
        console.log(`Nomes que começam com "${letra}":`);
        for (let i = 0; i < nomesFiltrados.length; i++){
            console.log(`${i + 1}: ${nomesFiltrados[i]}`);
        }
    }
    else {
        console.log(`Nenhum nome encontrado que comece com "${letra}"`);
    }
}
// BUSCAR POR NOME ESPECIFICO
let buscarNomeEspecifico = function(){
    let nomeBusca = prompt("Informe o nome a ser buscado:");
    let nomeEncontrado = nomes.find(nome => nome === nomeBusca);
    if (nomeEncontrado) {
        console.log(`O Nome: ${nomeEncontrado} está na lista.`);
    } else {
        console.log(`O Nome: ${nomeBusca} não foi encontrado.`);
    }
}
// TRANSFORMAR NOMES PARA MAIUSCULAS
let transformarNomes = function(){
    let nomesTransformados = nomes.map(nome => nome.toUpperCase());
    console.log("Nomes transformados para maiúsculas:");
    for (let i = 0; i < nomesTransformados.length; i++) {
        console.log(`${i + 1}: ${nomesTransformados[i]}`);
    }
}

// VERIFICAR CONDIÇÕES DE CARACTERES
let verificarCondicoes = function(){
    let resultado = nomes.every(nome => nome.length > 3);
    console.log(`Todos os nomes têm mais de 3 caracteres? ${resultado}`);
}

let menu = function(){
    op = parseInt(prompt("Menu de Opções:\n1 - Adicionar Nome\n2 - Filtrar Nomes por Letra Inicial\n3 - Buscar Nome Específico\n4 - Transformar Nomes para Maiúsculas\n5 - Verificar Condições de Caracteres\n0 - Sair\n[Escolha uma opção]:"));
    
    switch (op) {
        case 1:
            adicionarNome();
            break;
        case 2:
            filtrarNomesLetra();
            break;
        case 3:
            buscarNomeEspecifico();
            break;
        case 4:
            transformarNomes();
            break;
        case 5:
            verificarCondicoes();
            break;
        case 0:
            console.log("Saindo do programa... ");
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
    }
}

while (op != 0) {
    menu();
    console.log("\n");
}