const objnome = document.getElementsByTagName("input")[0].value;
const objidade = document.getElementsByTagName("input")[1].value;
const btnsalvar = document.getElementById("salvar");

const objdiv = document.getElementsByTagName("div")

function salvar(){
    try{
        if (objnome.length<3){
            throw new Error("Nome com menos de 3 letras");
        }
        objdiv[0].innerHTML += `Nome: ${objnome}`;        
    }
    catch(erro){
        console.error("💩 Erro:",erro.message)
        console.error("💩 Erro:",erro.stack)
    }
    try{
        if (parseInt(objidade) < 0 || objidade < 18){
            throw new Error("Idade menor que [zero] ou menor que [18]");
        }
        objdiv[1].innerHTML += `Idade: ${objidade}`;        
    }
    catch(error){
        console.error("👻 Erro:",error.message)
        console.error("👻 Erro:",error.stack)
    }
}

