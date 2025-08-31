const principais = document.getElementsByTagName("main");
principais[0].innerHTML = `<h2>Este H2 Está interno a Tag Main</h2><br/>`;
principais[0].innerText += '<h2> Este NÃO é um elemento H2</h2>';
principais[0].innerHTML += `<h2>Este H2 Está interno a Tag Main</h2><br/>`;

principais[0].innerHTML += `
        <nav>
            <a href="#">Cadastrar</a>
            <a href="#">Relatorios</a>
            <a href="#">Finalizar</a>
        </nav>
        <br/>
`;

//Criando atraves de metodos Js
const meuH3 = document.createElement("h3");
meuH3.textContent = "Sou o H3";
principais[0].appendChild(meuH3)
meuH3.style.border = "3px solid blue"
meuH3.onclick = function() {alert("Você clicou no H3!!!")};//Adicionar atributo

//Adicionar Atributos
const listaLinks = document.getElementsByTagName("a");
listaLinks[0].setAttribute("href","https://google.com");
listaLinks[1].setAttribute("href","https://bing.com");
listaLinks[2].setAttribute("href","https://duckduckgo.com");


//

// listaLinks[0].onclick = (event) => {
//     event.preventDefault();
//     alert("Link não autorizado!!!");
// };

listaLinks[0].addEventListener("click", function(event){
    event.preventDefault();
    alert("Link Não autorizado!!!")
});

// principais[0].addEventListener("keydown",(e)=>alert(`Tecla: ${e.code}`));
// document.body.addEventListener("keydown",(e)=>alert(`Tecla: ${e.code} = ${e.key}`));


meuH3.addEventListener("mousemove",(e)=>(console.log(e.clientX, e.clientY)))

principais[0].removeChild(meuH3);








//procurar sites de analise de organiograma dos portais