/*
Crie um pequeno programa em JavaScript que simule um sistema simples de notas escolares. Seu código deve:
*Declarar um objeto aluno com as seguintes propriedades:
    -nome (string)
    -idade (number)
    -notas (array de 3 números)

*Possuir um método calcularMedia() que retorna a média das notas;
*Utilizar desestruturação para acessar nome e idade;
*Usar o spread operator para adicionar uma nova nota ao array original;
*Criar uma função chamada verificarSituacao que:
    -Receba a média como parâmetro
    -Verifique se o aluno está aprovado (média ≥ 7) ou reprovado
    -Retorne uma mensagem adequada
    -Utilizar um loop para exibir todas as notas no console.

Exibir no console:
    -Nome e idade do aluno
    -Todas as notas
    -A média final
    -A situação (aprovado ou reprovado)
*/

// -------classe aluno ------------------------------------
class Aluno {
    constructor(nome, idade, notas) {
        this.nome = nome;
        this.idade = idade;
        this.notas = notas;
    }
    // ============= MÉTODOS  - calcular media ==============
    calcularMedia() {
        const { notas } = this;
        const soma = notas.reduce((acc, nota) => acc + nota, 0);
        return soma / notas.length;
    }
}
// -------------- Função verificar media ----------------------
function verificarSituacao(media) {
    if (media >= 7) {
        return "Aprovado";
    } else {
        return "Reprovado";
    }
}
// ----------------Objeto - Novo aluno -------------------------
const aluno1 = new Aluno("João", 15, [7, 8, 9]);
const aluno2 = new Aluno("Maria", 14, [6, 4, 5]);
// ------- Spread operator - adicionar mais uma nota -----------
aluno1.notas = [...aluno1.notas, 10];
aluno1.notas = [...aluno1.notas, 5];
// ----------- Desestruturacao ---------------------------------
const {nome, idade} = aluno1;
console.log('------ Dados aluno [Desestruturacao] ------')
console.log(`Nome: ${nome}, Idade: ${idade}`);
// ----------- Exibir no console -------------------------------
console.log('------ Notas aluno ------')
function exibirNotas(aluno) {
    aluno.notas.forEach((nota, index) => {
        console.log(`Nota ${index + 1}: ${nota}`);
    });
    const media = aluno.calcularMedia();
    console.log(`Média: ${media}`);
    console.log(`Situação: ${verificarSituacao(media)}`);
}
exibirNotas(aluno1);
exibirNotas(aluno2);