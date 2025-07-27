/*
 Explique o que são objetos literais em JavaScript e mostre um exemplo prático de um objeto chamado aluno, que contenha as seguintes propriedades e métodos:

nome (string)
notas (array de números)
calcularMedia() (método que retorna a média das notas)
Além disso, utilize a desestruturação para acessar o nome do aluno, e o spread operator para adicionar uma nova nota ao array original.
*/

// Objetos literais são estruturas de dados que permitem armazenar atributos(propriedades) e funções(métodos) relacionados a um determinado conceito(o objeto). Eles são definidos usando chaves `{}`.

// --- Construcao de um objeto: ---
const alunos = {
    nome: "Joao",
    notas: [5.25,7.1],
    somarNotas(){
        return this.notas.reduce((acc,nota)=>acc+nota,0)
    },
    calcularMedia(){
        return this.somarNotas()/this.notas.length
    }
};


// --- Consulta de dados por desestruturacao ---
const exibirNomeAluno = ({nome})=>{
    console.log(`Nome do aluno: ${nome}`)
}

exibirNomeAluno(alunos);
// --- Inclusao de dados com SPREAD operator ---

const extrairNotas = ({notas})=>{
    notasA = notas;
    novasNotas = [7.5,8.1,9.9];
    notas = [...notasA, ...novasNotas];
    console.log(`Notas do aluno: ${notas}`);
};

extrairNotas(alunos);

// --- Exibicao da media do aluno ---
console.log(`Media do aluno: ${alunos.calcularMedia()}`);
