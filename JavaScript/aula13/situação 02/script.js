let nome = null;
try {
    console.log(nome.toUpperCase());//Tentativa de chamar um metodo em um valor nulo
}
catch(error){
    console.error("🙅🏾‍♂️ Ocorreu um erro:",error.message);
}
