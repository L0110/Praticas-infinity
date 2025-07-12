const nomes = ["Ana","Martha","Clara","Pedro","Caio","Matheus","Thiago"]
const numeros = [6,1,12,2,3,4,5,8,9,10,11,7]
numeros.forEach(valor => { console.log(valor)});

const masculino = nomes.slice(3,nomes.length);

nomes.sort();
numeros.sort();
console.log(nomes);
nomes.forEach(valor => { console.log(valor)});

nomes.reverse();
console.log(nomes);
nomes.forEach(valor => { console.log(valor)});
console.log(numeros);
numeros.forEach(valor => { console.log(valor)});