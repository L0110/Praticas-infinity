const numeros = [1,2,3,4,5,6,7,8,9,10];
const idades = [11,22,33,44,55,66,17,15,19,65,28,42];
const animais = ["Tamanduá","Cachorro","Mamaco","Lebre","Pato","Gato"];

// localizando uma tag para manipular
const objH1 = document.querySelector("h1");
const objH2 = document.querySelector("h2");

// reduce(acumulador,itemAtualDaLista,valorInicial)
// console.log(numeros.reduce((acumulador,valor) => acumulador + valor));
let soma = numeros.reduce((acumulador,valor) => acumulador + valor);
let multiplicacao = numeros.reduce((acumulador,valor) => acumulador * valor);
let divisao = numeros.reduce((acumulador,valor) => acumulador / valor);
let subtracao = numeros.reduce((acumulador,valor) => acumulador - valor);
console.log(soma);
console.log(multiplicacao);
console.log(divisao);
console.log(subtracao);

objH2.innerHTML += `Soma: ${soma}<br/>`;
objH2.innerHTML += `multiplicação: ${multiplicacao}<br/>`;
objH2.innerHTML += `subtração: ${divisao}<br/>`;
objH2.innerHTML += `subtração: ${subtracao}<br/>`;