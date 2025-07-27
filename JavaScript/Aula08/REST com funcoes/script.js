function somar(...numeros){
    return numeros.reduce((acc,num)=>acc+num,0);
}
console.log(somar(1,2,3,4));


//-----------------------------------
const ExibirDetalhesFilme = ({titulo,diretor,...detalhes})=>{
    console.log(`Titulo: ${titulo}`);
    console.log(`Diretor: ${diretor}`);
    console.log(`Outros detalhes: ${detalhes}`);
}

const filme = {
    titulo: "Inseption",
    diretor: "Cristopher Nolan",
    ano: 2010,
    genero: "Ficção Científica",
    duração: "148 minutos"
};

ExibirDetalhesFilme(filme);
