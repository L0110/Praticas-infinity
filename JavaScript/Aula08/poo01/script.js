// objeto do tipo (classe) 'Array':
const a = Array();
// OU const a = [];

// propriedade do array
console.log(a.length);

// Objeto literal = objeto personalisado -> Definimos as propriedades dos nossos objetos
const carro = {
    //Atributos:
    marca: "BYD",
    cor: "Verde",
    motor: "Eletrico",
    maxima: 220,
    peso: 1234.5,
    vAtual: 0,
    //Metodos:
    acelerar:function(){
        this.vAtual += 10;
        return `Estou acelerando o ${this.marca}...\n Velocidade atual: ${this.vAtual}`;
    },
    frear(){
        return `Estou freiando o ${this.marca}...`;
    },
    travar(){
        if (this.trava === true){
            this.trava = false;
        } else{
            this.trava = true;
        };
        return `Trava da porta: ${this.trava}`;
    }
};
/*
        if (vAtual<maxima){
            vAtual += 10;
        } else {
        }
*/


console.log("---Propriedades do carro---")/
console.log("Cor: ",carro.cor);

carro.portas = 5; //Adicionando novos atributos/propriedades
carro.trava = false;
console.log("*-*-*-*-*-*-*-*-*-*-*");
console.log(carro);
delete carro.peso; //Excluindo atributos
console.log("*-*-*-*-*-*-*-*-*-*-*");
carro.cor = "Vermelho"; //Alteração de valores de atributos
console.log(carro);

console.log("🚗<<<<<<<<<<<<<<<<<<<<<<<<");
console.log(carro.acelerar());
console.log(carro.frear());
console.log(carro.travar());

/* lista de 
const arrayPessoas = [
    pessoa,
    pessoa,
    pessoa
]
*/


// Padrão ECMA Script (ES2016)
/*atributos/propriedades
exemplos:
nome
velocidade
arma
*/

/*
Ações/comportamentos -> metodos/funções
exemplos:
acelerar
andar
comer
*/