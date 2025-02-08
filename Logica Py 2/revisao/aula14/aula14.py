class Pessoas:
    def __init__(self,nome,telefone,email):
            self.nome = nome
            self.telefone = telefone
            self.email = email

class Clientes(Pessoas):
    cod:int = 0
    def __init__(self,nome,telefone,email,codigo):
        super().__init__(nome,telefone,email)
        self.codigo = codigo
        

    def gerar_id(self):
        cod += 1
        self.codigo = cod

class Edificio:
    

class Quartos:
    def __init__(self,porta,tipo,preco,status):
        self.porta = porta
        self.tipo = tipo
        self.preco = preco
        self.__disponivel = True

    def tipoQuarto(numSala,andaresEdificio):
        single = ['01','03','05','07']
        double = ['08','09','11','12']
        suite = ['02','04','06','10']
        andar = int(numSala[:-2])

    andaresEdificio = list(range(1,17))      
    
    single_preco = 100
    double_preco = 200
    suite = 400
    
    manutenção
    limeza
    ocupado
    
    livre

class Reservas():
    def __init__(self,hospede,uh,checkIn,checkOut,status):
        self.hospede = hospede
        self.uh = uh
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.statusReserva = status

    cancelado
    finalizado
    pendente

    ativo


class GerenciadorDeReservas:
    codigo:int = 0
    
    def __init__(self,pedido):
        self.pedido = pedido
    
    def gerar_pedido(self):
        codigo += 1
        self.pedido = codigo