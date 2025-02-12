class Empresas:
    
    def __init__(self):
        self.funcionarios = []

    def adicionar(self, obj_func):
        self.funcionarios.append(obj_func)

    def remover(self, obj_func):
        self.funcionarios.remove(obj_func)
    
    def listar(self,):
        for func in self.funcionarios:
            print(f"ID: {func.cod}, Funcionario: {func.nome}, Cargo: {func.cargo}, Salário: R$ {func.salario}")

class Funcionarios:

    def __init__(self,cod, nome, cargo, sal):
        self.cod = cod
        self.nome = nome
        self.cargo = cargo
        self.salario = sal
        contador = 0


ana = Funcionarios(1,"Ana","Analista",4444)
zeca = Funcionarios(2,"Zeca","Zelador",1400)
guanabara = Empresas()


print("Funcionarios")
guanabara.adicionar(ana)
guanabara.adicionar(zeca)


guanabara.listar()
print("Removendo...")
guanabara.remover(zeca)
print("Funcionarios")
guanabara.listar()


