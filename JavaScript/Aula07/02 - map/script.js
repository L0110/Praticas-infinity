const numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13];
const animais = ["Tamanduá","Cachorro","Mamaco","Lebre","Pato","Gato"];

// localizando uma tag para manipular
const objH1 = document.querySelector("h1");
const objH2 = document.querySelector("h2");

let b = numeros.map((valor,indice)=> `valor: ${valor} ➡ Indice: ${indice} <br/>`);
let q = numeros.map((valor)=>`valor: ${valor} ➡ ao quadrado: ${valor*valor} <br/>`);

console.log(b);
objH1.innerHTML += b;
console.log(q);
objH2.innerHTML += q;

