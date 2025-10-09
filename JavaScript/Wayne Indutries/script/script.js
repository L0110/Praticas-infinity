/* 
Sistema de Gerenciamento de Segurança:
 - Desenvolva um sistema de controle de acesso que permita apenas
 usuários autorizados a acessar áreas restritas das instalações das Indústrias
 Wayne.
 - Implemente autenticação e autorização para diferentes tipos de usuários,
 como funcionários, gerentes e administradores de segurança.
 
 Gestão de Recursos:
 Desenvolva uma interface para gerenciar recursos internos, como:
 - inventário de equipamentos,
 - veículos,
 - dispositivos de segurança.
 Permita que os administradores possam:
 - adicionar, 
 - remover, 
 - atualizar
 informações sobre esses recursos de forma eficiente.

 Dashboard de Visualização:
 Crie um painel de controle visualmente atraente que exiba dados relevantes
 sobre segurança, recursos e atividades dentro das Indústrias Wayne.

*/

// ---------[OBJETO INVENTÁRIO]-------------
/*
Tipos de itens: Equipamento, Veículo, Dispositivo de Segurança, Material de escritorio, Uso e consumo, Outros
Armazem: Almoxarifado Central, Depósito Secundário, Oficina, Galpão Caverna dos Wayne, Outros
Localização: Prédio A, Prédio B, Prédio C, Estacionamento, Área Externa, Almoxarifado Central, Depósito Secundário, Oficina, Galpão Caverna dos Wayne, Outros
Requisição: Nome do funcionário ou departamento que requisitou o item
Observações: Campo para anotações adicionais sobre o item
*/
const inventario = {
    item: "",
    tipo: "",
    quantidade: 0,
    armazem: "",
    localizacao: "",
    id: 0,
    observacoes: "",
    // ---------[CADASTRO E EDIÇÃO]-------------
    // 
    adicionarItem() {
        // Lógica para adicionar item ao inventário
    },
    removerItem() {
        // Lógica para remover item do inventário
    },
    atualizarItem() {
        // Lógica para atualizar detalhes do item
    },
    listarItens() {
        // Lógica para listar todos os itens no inventário
    },
    filtrarItems() {
        // Lógica para filtrar itens com base em critérios específicos
    },
    requisitarItem() {
        // Lógica para requisitar um item do inventário
    },
    // -----------[SALVAMENTO E CARREGAMENTO - LOCAL STORAGE]-----------
    salvarInventario() {
        // Lógica para salvar o inventário no armazenamento local
    },
    carregarInventario() {
        // Lógica para carregar o inventário do armazenamento local
    },
    // ---------[ANÁLISE RESUMIDA DA TELA INICIAL]-------------
    contadorItensPorTipo() {
        // Lógica para contar itens por tipo
    },
    itensEmFalta() {
        // Lógica para identificar itens com quantidade baixa
    },
    itensComMaisQuantidade() {
        // Lógica para identificar itens com maior quantidade
    },
    itensComPoucaQuantidade() {
        // Lógica para identificar itens com menor quantidade
    }
}
// ---------[OBJETO PERFIL]-------------
/*
Credenciais: 
[Administrador]: Acesso total a todas as áreas e recursos.
[Gerente]: Controla acesso a áreas específicas e recursos, faz requisicoes e relatorios
[Funcionário]: Faz requisicoes e relatorios.
[Convidado]: Faz registro mas nao tem acesso a areas restritas ou ao sistema.
[Outros]: Faz registro mas nao tem acesso a areas restritas ou ao sistema.
*/
// Localização: Prédio A, Prédio B, Prédio C, Estacionamento, Área Externa, Outros
//entrada: Registro de horário de entrada
//saida: Registro de horário de saída
const perfil = {
    nome: "",
    email: "",
    senha: "",
    credencial: "",
    telefone: "",
    id: 0,
    localizacaoAutorizada: [""],
    localizacaoAtual: "",
    entrada: [{data: new Date().toLocaleString(), horario: new Date().toLocaleTimeString()}],
    saida: [{data: new Date().toLocaleString(), horario: new Date().toLocaleTimeString()}],
    // ---------[CADASTRO E EDIÇÃO(apenas administradores)]-------------
    cadastrarUsuario() {
        // Lógica para cadastrar um novo usuário
    },
    editarUsuario() {
        // Lógica para editar os dados do usuário
    },
    excluirUsuario() {
        // Lógica para excluir um usuário
    },
    visualizarUsuario() {
        // Lógica para visualizar os dados do usuário
    },
    // ---------[REGISTRO DE PONTO(Administradores e gerentes)]-------------
    incluirLocalizacauoAutorizada() {
        // Lógica para incluir localizações autorizadas para o usuário
    },
    removerLocalizacaoAutorizada() {
        // Lógica para remover localizações autorizadas para o usuário
    },
    registrarEntrada() {
        // Lógica para registrar horário de entrada
    },
    registrarSaida() {
        // Lógica para registrar horário de saída
    }
}
// ---------[OBJETO RELATÓRIOS]-------------
const relatorios = {
    gerarRelatorioDiario() {
        // Lógica para gerar um relatório diário
    },
    gerarRelatorioMensal() {
        // Lógica para gerar um relatório mensal
    },
    gerarRelatorioAnual() {
        // Lógica para gerar um relatório anual
    }
}

const localizacao = {
    nomeLocal: "",
    ocupado: false,
    id: 0,
    publico: false,
    armazem: false,
    endereco: {rua:"", numero: "", complemento: "", cidade: "", estado: "", cep: ""},
    // ---------[GERENCIAMENTO DE LOCAIS]-------------
    adicionarLocal(){
        // Lógica para adicionar um novo local
    },
    removerLocal(){
        // Lógica para remover um local
    },
    atualizarLocal(){
        // Lógica para atualizar detalhes do local
    },
    // ---------[MONITORAMENTO DE LOCALIZAÇÃO]-------------
    monitorarLocalizacao() {
        // Lógica para monitorar a localização do usuário
    }
}

const login = {
    autenticarUsuario() {
        // Lógica para autenticar o usuário
    },
    autorizarAcesso() {
        // Lógica para autorizar o acesso com base nas credenciais do usuário
    }
}
