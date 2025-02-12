from atv03 import (Empresas,Funcionarios,)


print("+"*6, "Novo funcionario", "+"*6)
def add_funcionario():
    Funcionario.contador += 1
    cod = Funcionario.contador
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    sal = input("Salário: R$ ")

Add_funcionario(Funcionarios(contador,nome,cargo,sal))