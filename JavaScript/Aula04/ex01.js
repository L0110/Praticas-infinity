let listafrutas = ["maçã","banana","laranja"]; //Array


//INDICE    00  -    01  -  02   -   03  -  04
//ELEMENTO  1   -  "STR" -  2    -  true - null  

//seletores de dados para tratar dados do html
document.getElementById("principal");
document.querySelector("principal");
//transforma em nodelist
document.querySelectorAll(".principal");


const listaNumeros = [1,2,3,4,5,6,7,8,9];
const arrayVazio = [];
console.log("Tamanho listaNumeros: ", listaNumeros.length);
console.log("Tamanho arrayVazio:",arrayVazio.length);

//CRUD
//INSERIR EM UM ARRAY:
//- inserir ao final:
console.log("inclusao do valor 10 no final do Arry:")
listaNumeros.push(10);
listaNumeros.push(11);
listaNumeros.push(12);
console.log("Tamanho: ", listaNumeros.length);

//- inserir no início:
console.log("inclusao do valor 10 no final do Arry:")
listaNumeros.unshift(0);
listaNumeros.unshift(-1);
console.log("Tamanho: ", listaNumeros.length);

//ALTERAR EM UM ARRAY:
//-alteração:
console.log(listaNumeros[4])
listaNumeros[4] = "quatro"

console.log("Impressao de valores do Array:")
for(let indice = 0; indice<listaNumeros.length; indice++){
    console.log(listaNumeros[indice]);
}
console.log("----------------------------------------------------");
//EXCLUIR EM UM ARRAY:
//-excluir ao final:
listaNumeros.pop();
//-excluir ao inicio:
listaNumeros.shift();

console.log("Impressao de valores do Arry:")
for(let indice = 0; indice<listaNumeros.length; indice++){
    console.log(listaNumeros[indice]);}

console.log("----------------------------------------------------");
//SPLICE = INCLUSÃO DE REMOÇÃO

const frutas = ["Maça","Banana","Laranja"];
for(let indice = 0; indice<frutas.length; indice++){
    console.log(frutas[indice]);}

console.log("----------------------------------------------------");
//frutas.splice(INDICE DE EXCLUSAO , QUANTIDADES DE ITENS A EXCLUIR A PARTIR DO INDICE , ITENS A SEREM INCLUIDOS[OPCIONAL]");
frutas.splice(1,0,"Morango","Uva"); // MAÇA MORANGO UVA BANANA LARANJA

for(let indice = 0; indice<frutas.length; indice++){
    console.log(frutas[indice]);}

frutas.splice(2,2);//EXLUI UVA E BANANA

console.log("----------------------------------------------------");
for(let indice = 0; indice<frutas.length; indice++){
    console.log(frutas[indice]);}

    //conversor de listas par arry
    // array.from(HTMLAllCollection);
console.log("******************************************");
//ALTERNATIVA AO FOR (só funciona em arrays)
frutas.forEach(valor => { console.log(valor)});
console.log("******************************************");
