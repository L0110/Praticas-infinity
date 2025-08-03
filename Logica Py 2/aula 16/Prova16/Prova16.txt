/*
[PYIA-A16] Crie uma tabela chamada Produtos que contenha quatro colunas: ProdutoID, 
NomeProduto, Quantidade e Preco. A coluna ProdutoID deve ser um identificador único 
para cada produto, a coluna NomeProduto deve armazenar o nome do produto, a coluna 
Quantidade deve indicar a quantidade disponível do produto, e a coluna Preco deve 
representar o preço do produto. Após criar a tabela, insira três registros diferentes, 
cada um representando um produto distinto, incluindo valores específicos para ProdutoID, 
NomeProduto, Quantidade e Preco.
*/

CREATE TABLE IF NOT EXISTS Produtos(
	ProdutoID INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(140),
    Quantidade TINYINT,
    Preco FLOAT
);

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Doritos 25g",10,14.50);
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Guarana Jesus 200ml",12,5.0);
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Mel 500g",2,30.00);

SELECT * FROM Produtos;