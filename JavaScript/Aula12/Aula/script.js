// setItem() - salva item
// getItem() - consulta
// removeItem() - remove item
// clear() Limpa todo o estoqueSotorage


// localStorage.setItem('CHAVE','VALOR');
localStorage.setItem('nomeEX','João');
// console.log(nomeEX);
// localStorage.removeItem('nomeEX');


// ----------------------------------------

function salvar(){
    const nomeStr = document.getElementById("nome").value;
    const idadeStr = document.getElementById("idade").value;
    const vlrH3 = document.getElementsByTagName("h3")[0];
    localStorage.setItem("nome",nomeStr)//SetItem - salva a 'chave' e o 'valor' no LS     
    localStorage.setItem("idade",idadeStr)//SetItem - salva a 'chave' e o 'valor' no LS     
    vlrH3.innerHTML += `Nome: ${nomeStr} - Idade: ${idadeStr}<br/>`;
}

function exibir(){
    const nomeStr = localStorage.getItem("nome");
    const idadeStr = localStorage.getItem("idade");
    const vlrH2 = document.getElementsByTagName("h2")[0];
    vlrH2.innerHTML += `Nome: ${nomeStr} - Idade: ${idadeStr}<br/>`;
}
function remover(){
    localStorage.removeItem("nome");
    localStorage.removeItem("idade");
}


// const objNome = document.getElementsByTagName("input")[0];
// const objIdade = document.getElementsByTagName("input")[1];

