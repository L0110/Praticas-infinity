// Nosso array numperico
const numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13];
const animais = ["Tamanduá","Cachorro","Mamaco","Lebre","Pato","Gato"];
// localizando uma tag para manipular
const objH1 = document.querySelector("h1");
// impressão no console e na pagina - forEach = para cada
numeros.forEach((numero,index)=>{
    console.log("O elemento no indice "+index+" é "+numero)
});
numeros.forEach((valor)=>{
    objH1.innerHTML += `${valor} ▶ <br/>`;
});

animais.forEach((bicho,index)=>{
    objH1.innerHTML += `${index} ▶ ${bicho} <br/>`;
});

numero,forEach((valor,index)=>console.log(v*v));
