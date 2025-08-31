//TRATAMENTO DE EXCEÇÃO
//try...catch
function dividir(numerador, denominador){
    try{
    //CODIGO A SER EXECUTADP COM POTENCIAL DE ERRO
    if (denominador === 0){
        throw new Error("Divisão por zero!");
    }
    return numerador / denominador;
    }
    catch (error){
    //GERENCIAMENTO DE ERRO. É EXECUTADO CASO O ERRO OCORRA
    // alert("123 - Erro detectado, recarregue a API")
    console.error("Erro",error.message);
    }
    finally{
    //SEMPRE Será executado [opcional]
    console.log("Operação de divisão finalizada");
    }
}
dividir(10,0)