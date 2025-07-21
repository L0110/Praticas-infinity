const numeros = [1,2,3,4,5,6,7,8,9,10];
const idades = [11,22,33,44,55,66,17,15,19,65,28,42];
const animais = ["Tamanduá","Cachorro","Mamaco","Lebre","Pato","Gato"];
const notas = [3.4,4.0,2.0,7.5,9.9,10];

// localizando uma tag para manipular
const objH1 = document.querySelector("h1");
const objH2 = document.querySelector("h2");

const teste = [3.4,4.0,2.0,7.5,9.9].some(nota => nota === 10);
console.log(teste);

objH2.innerHTML += `${teste} <br/>`;
objH2.innerHTML += notas.some(nota => nota >= 9.0)


if (notas.some(nota => nota >= 10.0)){
    objH2.innerHTML += "<br/>Alguém tirou 10 ✨";
}
else {
    objH2.innerHTML += "ninguém tirou 10 😒";
}
// procurar ecma script

