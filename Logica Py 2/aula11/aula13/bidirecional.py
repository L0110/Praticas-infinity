class Biblioitecas:
    def __init__(self,nome):
        self.nome = nome
        self.livros = []
    
    def inserir_livros(self,obj_livro):
        self.livros.append(obj_livro)

class Livros:
    def __init__(self,titulo):
        self.titulo = titulo
        self.bibliotecas = []

    def inserir_biblioteca(self, obj_biblioteca):
        self.bibliotecas.append(obj_biblioteca)

#=================================================
barris = Biblioitecas("Biblioteca dos Barris")
central = Biblioitecas("Biblioterca do Colégio Central")

coach = Livros("Livro indiscutivel com a solução universal")
camoes = Livros("Os Lusianas")

barris.inserir_livros(coach)
barris.inserir_livros(camoes)

coach.inserir_biblioteca(barris)
camoes.inserir_biblioteca(central)
camoes.inserir_biblioteca(barris)


for livro in barris.livros:
    print(f"Título: {livro.titulo}")

print("")
for biblioteca in camoes.bibliotecas:
    print(f"nome: {biblioteca.nome}")