

// 1) Definindo a quantidade de Estudantes da turma:
// 2) Inserindo nomes e notas:
// 3) Relatório de análises: Ordenar por Nota
// 4) Cria o objeto main (Principal) do HTML:
// 5) Listar nomes e notas ordenados por Notas: (<li>)
// 6) Alunos aprovados com nota Maior ou igual a 6:
// 7) Média da Turma: (.reduce ())
// 8) Verificação se todos os alunos têm nota maior que 3: (. every() e Ternário)
// 9) Verificação se pelo menos um tirou nota 10: ( .some() e Ternário)
// 10) Nome do primeiro aluno que tirou menos que 5: (.find ())

//criar um objeto 'HTMLCollection' Js da <section>
const sessao = Array.from(document.getElementsByTagName('section'));

//1 - Quantidade de estudantes:
let quantidadeEstudantes = parseInt(prompt("Digite a quantidade de Estudantes: "));

sessao[0].innerHTML = `Quantidade de <em>Alunos</em> = ${quantidadeEstudantes} <hr />`;

//2 - Inserindo Nomes e Notas:
//Ex: [["Vinicius",6.5],["Caio",10],["Tiago",9.5]];

const alunosNotas = [];

for(let indice = 0; indice < quantidadeEstudantes; indice++){
    let nome = prompt("Digite o NOME do Estudante: ").toUpperCase();
    let nota = parseFloat(prompt("Digite a NOTA (0 a 10): "));
    alunosNotas.push([nome, nota]);   
}

//3 - Ordenar por Nota:
alunosNotas.sort((a,b) => a[1] - b[1]);
//alunosNotas.reverse();


//5 - Listar Nomes e Notas:
for(aluno of alunosNotas){
    sessao[0].innerHTML += `Aluno: ${aluno[0]} - Nota ${aluno[1]} <br/>`;
}

//6 - Alunos Aprovados com nota maior ou igual a 6:
sessao[0].innerHTML += "<hr /><br/> Alunos aprovados: <br/><br/>"

alunosNotas.forEach(
    //argumento => teste ? return verdadeiro : return falso
    item => (item[1]>=6) ? sessao[0].innerHTML += `<li> Aluno: ${item[0]} </li><br />`:""

);

//7 - Media da turma usando (.reduce())
//recebendo dois argumentos e um valor inicial(opcional)
let soma = alunosNotas.reduce(
    (somatoria, item,) => somatoria + item[1]
);

let media = soma / quantidadeEstudantes;
// OU: let media = soma / alunosNotas.length
sessao[0].innerHTML += `<hr /><br/> Média da turma: ${media} <br/><br/>`;

//8- Verificação se há alunos com nota maior que 3 usando (. every() e Ternário)