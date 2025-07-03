/*
Crie um sistema em JavaScript que utilize os conceitos de operadores ternários, estruturas switch e operadores lógicos para classificar e exibir mensagens baseadas na idade e no status do usuário.

Requisitos do Projeto:

* Solicite ao usuário a idade e o status de registro (registrado ou não registrado) utilizando prompt().
* Use um operador ternário para determinar se o usuário é maior de idade ou menor de idade.
* Utilize uma estrutura switch para exibir uma mensagem personalizada com base no status do usuário:

- "registrado": Exibir mensagem de boas-vindas.
- "não registrado": Exibir mensagem para completar o registro.
- Qualquer outro valor: Exibir "Status desconhecido."
- Adicione uma lógica com operadores lógicos para verificar:
- Se o usuário é maior de idade e registrado, exiba uma mensagem de acesso completo.
- Se o usuário é menor de idade ou não registrado, exiba uma mensagem de acesso limitado.
*/
// Mensagens pre configuradas
const cab01 = "*-------[REGISTRO]--------*"; 
const cab02 = "*----------[O]------------*";
const cab03 = "*----------[X]------------*";
const q1 = "Informe sua idade: ";
const q2 = "Possui registro?(S/N): ";
const ola = "Seja Bem-vindo!";
const falha = "Alguns dados impedem de prosseguir...";

// variaveis
let idade = null;
let registro = null;
let statusRegistro = null;
let testeIdade = null;

// recebendo a entrada da idade
console.log(cab01);
idade = prompt(cab01+"\n"+q1);
// Recebendo status de cadatro, caso o usuario seja maior de idade
if (idade >= 18){
    registro = prompt(cab01+"\n"+q2).toUpperCase();
}
// Definindo mensagem com idade como contexto
if (idade != null){
    if (idade >= 18){
    testeIdade = 1;
    } else{
    testeIdade = 2;
    }
}

switch(testeIdade){
    case 1:
        msgIdade = "Maior de idade";
        break;
    case 2:
        msgIdade = "Menor de idade";
        break;
    default:
        msgIdade = "Idade nao informada";
}
// Definindo mensagem com status de registro como contexto
switch(registro){
    case "S":
        statusRegistro = "Registrado ✅";
        break;
    case "N":
        statusRegistro = "Sem registro ❌";
        break;
    default:
        statusRegistro = "Não informado";
}
    
let msgRegistro = (registro == "S")?"Registro ATIVO":"Usuario SEM REGISTRO";

// impressao dos dados processados
console.log("Registro: ", statusRegistro);
console.log("Idade: ",idade);

// impressao dos dados processados, com base nos dados processados
let informe = (registro == "S" && idade >= 18)? true : false;

let cabRes = (informe == true) ? cab02 : cab03;
let saudacao = (informe == true) ? ola : falha;
console.log(cabRes,"\n",saudacao,"\n");

if (informe == false && idade < 18){
        console.log(msgIdade);
    } else if (informe == true){
        console.log(msgIdade);
    }

console.log(msgRegistro);
