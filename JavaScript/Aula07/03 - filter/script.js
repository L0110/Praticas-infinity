const numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13];
const idades = [11,22,33,44,55,66,17,15,19,65,28,42];
const animais = ["Tamanduá","Cachorro","Mamaco","Lebre","Pato","Gato"];

// localizando uma tag para manipular
const objH1 = document.querySelector("h1");
const objH2 = document.querySelector("h2");

let menores = idades.filter((idade)=>idade<18);
let maiores = idades.filter((idade)=>idade>=18);
console.log(`Menores de idade: ${menores}`);
objH2.innerHTML += `Menor de idade: ${menores}<br/>`;
objH2.innerHTML += `Maior de idade: ${maiores}<br/>`;