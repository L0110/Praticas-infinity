/*
 Desenvolva uma aplicação web simples utilizando Eventos DOM, atribuição de eventos e o método preventDefault() para gerenciar a interação com um formulário. O projeto permitirá que o usuário preencha e envie informações sem recarregar a página, validando os dados antes do seu envio.

Requisitos do Projeto:
a) Um formulário com os seguintes elementos:
- Um campo de texto para o nome de usuário e senha.
- Um campo para telefone.
- Um campo para data de nascimento.
- Um campo de e-mail.
- Um botão para envio.

b) Atribuir Eventos ao Formulário:
- Use o método addEventListener() para detectar o evento de envio do formulário (submit).

c) Prevenindo Comportamento Padrão:
- No evento de envio, utilize preventDefault() para impedir que a página seja recarregada ao enviar o formulário.

d) Validação Simples:
- Verifique se os campos não estão vazios.
- Caso um campo esteja vazio, exiba uma mensagem de erro no console e não permita o envio.
- Utilize o "type" correspondente para cada tipo de dado a ser inserido.

e) Adicionando Informações Dinamicamente:
- Caso os dados sejam válidos, crie um novo elemento HTML com os dados preenchidos.
- Use o método createElement() para criar os elementos dinamicamente e appendChild() para adicioná-los à lista.

f) Botão de Reset:
- Adicione um botão "Limpar Lista" que, ao ser clicado, remova todos os elementos adicionados à lista.
- Use o método innerHTML = "" para limpar a lista.
*/

// ---------- Criando container da tabela ----------
const listaCadastral = [];
const tabelaContainer = document.getElementById("tabela-container") || (() => {
    const div = document.createElement("div");
    div.classList.add("container");
    div.id = "tabela-container";
    document.body.appendChild(div);
    return div;
})();

// ---------- Criando tabela ----------
function criarTabela() {
    tabelaContainer.innerHTML = "";
    if (listaCadastral.length === 0) return;
    
    const tabela = document.createElement("table");
    // ---------- Adicionando cabecalho à tabela ----------
    const cabecalho = document.createElement("tr");
    cabecalho.innerHTML = `
        <th>Nome</th>
        <th>Senha</th>
        <th>Telefone</th>
        <th>Data de Nascimento</th>
        <th>Email</th>
        <th>Ações</th>
    `;
    tabela.appendChild(cabecalho);

    // ---------- Criando linhas da tabela ----------
    listaCadastral.forEach((item, idx) => {
        const linha = document.createElement("tr");
        linha.innerHTML = `
            <td>${item.nome}</td>
            <td>${item.senha}</td>
            <td>${item.telefone}</td>
            <td>${item.dataNascimento}</td>
            <td>${item.email}</td>
            <td><button class="btn-remover" data-idx="${idx}">Remover</button></td>
        `;

        // ---------- Adicionando linha à tabela ----------
        tabela.appendChild(linha);
    });
    // ---------- Adicionando tabela ao container ----------
    tabelaContainer.appendChild(tabela);

    // ---------- Adicionando funcao ao botao remover ----------
    tabela.querySelectorAll(".btn-remover").forEach(btn => {
        btn.addEventListener("click", function() {
            const idx = parseInt(this.getAttribute("data-idx"));
            listaCadastral.splice(idx, 1);
            criarTabela();
        });
    });
}
// ---------- Criacao do botao enviar ----------
const btnEnviar = document.getElementById("btn-enviar");
btnEnviar.addEventListener("click", function(event){
    event.preventDefault();

    const nome = document.getElementById("nome-usuario").value;
    const senha = document.getElementById("senha").value;
    const telefone = document.getElementById("telefone").value;
    const dataNascimento = document.getElementById("data-nascimento").value;
    const email = document.getElementById("email").value;
    // ---------- Teste de campos vazios ----------
    if(nome === "" || senha === "" || telefone === "" || dataNascimento === "" || email === ""){
        console.error("Um ou mais campos nao foram preenchidos");
        return;
    }
    // ---------- Inclusao de dados na lista ----------
    listaCadastral.push({
        nome: nome,
        senha: senha,
        telefone: telefone,
        dataNascimento: dataNascimento,
        email: email
    });

    criarTabela();
});

// ---------- Botao limpar lista agora é criado dinamicamente na tabela ----------
function adicionarBotaoLimpar(tabela) {
    const rodape = document.createElement("tr");
    rodape.innerHTML = `
        <td colspan="6">
            <button id="btn-limpar-lista">Limpar Lista</button>
        </td>
    `;
    tabela.appendChild(rodape);

    // Adiciona o event listener ao botão recém-criado
    rodape.querySelector("#btn-limpar-lista").addEventListener("click", function() {
        listaCadastral.length = 0;
        criarTabela();
    });
}

// Modifique a função criarTabela para adicionar o botão ao final da tabela
const originalCriarTabela = criarTabela;
criarTabela = function() {
    tabelaContainer.innerHTML = "";
    if (listaCadastral.length === 0) return;

    const tabela = document.createElement("table");
    // ---------- Adicionando cabecalho à tabela ----------
    const cabecalho = document.createElement("tr");
    cabecalho.innerHTML = `
        <th>Nome</th>
        <th>Senha</th>
        <th>Telefone</th>
        <th>Data de Nascimento</th>
        <th>Email</th>
        <th>Ações</th>
    `;
    tabela.appendChild(cabecalho);

    // ---------- Criando linhas da tabela ----------
    listaCadastral.forEach((item, idx) => {
        const linha = document.createElement("tr");
        linha.innerHTML = `
            <td>${item.nome}</td>
            <td>${item.senha}</td>
            <td>${item.telefone}</td>
            <td>${item.dataNascimento}</td>
            <td>${item.email}</td>
            <td><button class="btn-remover" data-idx="${idx}">Remover</button></td>
        `;

        // ---------- Adicionando linha à tabela ----------
        tabela.appendChild(linha);
    });
    // ---------- Adicionando tabela ao container ----------
    tabelaContainer.appendChild(tabela);

    // ---------- Adicionando funcao ao botao remover ----------
    tabela.querySelectorAll(".btn-remover").forEach(btn => {
        btn.addEventListener("click", function() {
            const idx = parseInt(this.getAttribute("data-idx"));
            listaCadastral.splice(idx, 1);
            criarTabela();
        });
    });

    // ---------- Adicionando botao de limpar a lista no rodape ----------
    adicionarBotaoLimpar(tabela);
};
