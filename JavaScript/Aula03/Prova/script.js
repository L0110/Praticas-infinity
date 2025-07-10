/*
Crie um programa em JavaScript que combine o uso de while (true), for, e for...of para realizar operações iterativas. O programa deve solicitar entradas do usuário, processar os dados e exibir resultados em diferentes formatos.

Requisitos do Projeto:
* Coleta de Dados com while (true):
 - Solicite ao usuário uma sequência de nomes (ou qualquer outro tipo de dado) usando prompt().
 - O loop deve continuar até que o usuário insira uma palavra específica como "sair". Use break para encerrar o loop.

* Processamento com for:
 - Após coletar os dados, use um loop for para exibir os dados com índices. Exemplo: 1: Nome1

* Exibição com for...of: 
 - Use um loop for...of para exibir cada nome individualmente com uma mensagem personalizada, como "Bem-vindo(a), Nome!".
*/
nome = null;
repeticao = true;
listaNomes = [];

faixa = "*".repeat(10);
console.log(faixa,"Interacao com 'While'",faixa,"\n\n");
do{
    nome  = prompt("Insira um nome: [Digite SAIR para prosseguir]");
    if (nome === null) {
        alert("Você cancelou. Tente novamente!");
    }
    if (nome != null){
        teste = nome.toUpperCase();
        if (teste === "SAIR"){
            break;
        } else if(nome.trim() === ""){
            alert("Digite algo...");
        } else{
            listaNomes.push(nome);
            console.log("⭐ Nome adicionado! ⭐")
        }
    }
}while ( repeticao === true);

console.log(`${faixa} Exibicao de lista com 'For' ${faixa}\n\n`);
for (i=0; i<listaNomes.length; i++){
    console.log(i+1+":"+listaNomes[i]);
}

console.log(`${faixa} Exibicao de lista com 'For... of' ,${faixa}\n\n`);
for (listado of listaNomes){
    console.log(`Bem vindo(a), ${listado}!`)
} 