// Solicite ao usuario dois numeros usando o metodo prompt()
// realize as operações básicas(adição, subtração, multiplicação, divisão e resto) e exiba o resultado
// Utilize operadores de atribuição (como +=, -=, *=, /=, %=) para atualizar/reatribuir o valor de uma variavel com os resultados das operacoes
// Mostre o resultado de cada operação no console utilizando console.log()
let num1 = parseFloat(prompt("Digite o primeiro número:"));
let num2 = parseFloat(prompt("Digite o segundo número:"));

// Soma
let resultAdicao = num1;
resultAdicao += num2;
console.log(`Resultado da adição: ${resultAdicao}`);

// subtração
let resultsub = num1;
resultsub -= num2;
console.log(`Resultado da subtração: ${resultsub}`);


// Multiplicação
let resultMult = num1;
resultMult *= num2;
console.log(`Resultado da multiplicação: ${resultMult}`);


// Divisão
let resultDiv = num1;
resultDiv /= num2;
console.log(`Resultado da divisão: ${resultDiv}`);


// Resto
let resultResto = num1;
resultResto %= num2;
console.log(`Resultado do resto: ${resultResto}`);

