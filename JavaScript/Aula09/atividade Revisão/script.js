/*
=========================================
Criar um cadastro de alunos e notas:
=========================================

- Armazenar os dados (nome e nota) em um objeto (criar input e button)
- Criar um contador (imprimir da página, canto superior direito)
- Armazenar todos os objetos em um Array
- Filtrar os alunos que ficaram em RECUPERAÇÃO (notas menor ou igual a 6,0), imprimir em uma lista.
- Verificar se houve algum estudante que ficou com nota máxima (10), sim ou não.
- Calcular a média da turma (usar reduce() e length), imprimir na página.
- Estilizar a gosto a página.
*/

//listeners
const objAluno = document.querySelector("#aluno");
const objNota = document.querySelector("#nota");
const saida = document.querySelector("#saida");
const contagem = document.querySelector("#contador");
const botaoSalvar = document.querySelector("#incluir");
const botaoReprovados = document.querySelector("#btn-reprovado");
const botaoTodos = document.querySelector("#btn-todos-alunos");
botaoSalvar.addEventListener("click",adicionar);
// objAluno.addEventListener("input",mostrar);


// Lista de alunos da turma + nota media individual
//array global para armazenar todos os alunos
let turma = [];
let contador = turma.length
//contador
function chamarContagem(){
    contagem.innerHTML += `<br/> Contagem: ${contador}<br/><hr />`
}


//Aramazenando todos os dados no Array turma
function mostrar() {
   console.log(objAluno.value);
    saida.innerHTML = 'Lista de alunos';
    turma.forEach(
        (aluno) => {
            saida.innerHTML += `<li>${aluno.nome} - ${aluno.nota}</li>`
        }
    );
}
botaoSalvar.addEventListener("click",mostrar)

function adicionar(){
    const nomeAluno = objAluno.value.trim().toUpperCase();
    const notaAluno = parseFloat(objNota.value);
    
    const dados = {
        nome: nomeAluno,
        nota: notaAluno
    };
    turma.push(dados);
    console.log(turma);
    chamarContagem();
};


//Filtrar alunos em RECUPERAÇÃO (nota <= 6.0) imprimir em uma lista
botaoReprovados.addEventListener("click",exibirReprovados)
botaoTodos.addEventListener("click",mostrar)

function exibirReprovados(){
    const listaReprovados = turma.filter(
        aluno => aluno.nota <= 6.0
    );
    saida.innerHTML = 'Lista Reprovados';
    listaReprovados.forEach(
        (aluno) => {
            saida.innerHTML += `<li>${aluno.nome} - ${aluno.nota}</li>`
        }
    );
};