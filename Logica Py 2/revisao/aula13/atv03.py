"""
Crie uma classe Aluno em Python com atributos privados,
como nome, idade e matrícula. Implemente métodos
públicos para acessar e modificar esses atributos. Em
seguida, crie uma instância da classe e demonstre como
usar os métodos de acesso.
"""

class Alunos:
    def __init__(self, nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.__idade = 1

    @property
    def idade(self):
        return self.__idade 
    
    @idade.setter
    def idade(self,valor_idade):
        if ((self.__idade > 0) and (self.__idade < 200)):
            self.__idade = valor_idade
        else:
            print("!!!valor fora do escopo!!!")

#==================================================
zezim = Alunos("Zezim", "0001")
print(zezim.idade)
zezim.idade = 22
print(zezim.idade)