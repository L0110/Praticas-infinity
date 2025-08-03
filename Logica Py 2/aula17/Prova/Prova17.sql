/*
[PYIA-A17] Crie uma tabela chamada Estoque que contenha as seguintes colunas: 
EstoqueID, ProdutoID, FornecedorID, Quantidade e DataEntrada. A coluna EstoqueID 
deve ser um identificador único para cada registro no estoque. A coluna ProdutoID deve 
referenciar o identificador do produto correspondente na tabela de produtos, e a coluna 
FornecedorID deve referenciar o identificador do fornecedor na tabela de fornecedores, 
ambas atuando como chaves estrangeiras para estabelecer a relação com outras tabelas. A 
coluna Quantidade deve indicar a quantidade de produtos recebidos, e a coluna DataEntrada 
deve armazenar a data em que os produtos entraram no estoque. Para criar esta tabela e garantir 
as referências corretas, é necessário definir as chaves estrangeiras para ProdutoID e FornecedorID.

Após a criação da tabela, você pode utilizar operações de banco de dados como FULL OUTER JOIN para 
combinar informações de diferentes tabelas, GROUP BY para agrupar dados com base em uma ou mais colunas, 
e ALTER TABLE para modificar a estrutura da tabela, como adicionar ou alterar colunas.
*/
CREATE DATABASE IF NOT EXISTS Infinity_db;
USE Infinity_db;

CREATE TABLE IF NOT EXISTS Estoque(
	EstoqueID INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    ProdutoID INT,
    FornecedorID INT,
    FOREIGN KEY pID(ProdutoID) REFERENCES Produtos(ProdutoID),
    FOREIGN KEY fID(FornecedorID) REFERENCES Fornecedores(ID),
    Quantidade FLOAT,
    DataEntrada DATE
);

CREATE TABLE IF NOT EXISTS Produtos(
	ProdutoID INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
    NomeProduto VARCHAR(140),
    Quantidade TINYINT,
    Preco FLOAT
);

CREATE TABLE IF NOT EXISTS Fornecedores(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(140),
    Cidade VARCHAR(60)
);

SELECT * FROM Estoque;
SELECT * FROM Produtos;
SELECT * FROM Fornecedores;

INSERT INTO Fornecedores (Nome, Cidade) VALUES ("PepsiCO","Salvador"); /*1*/
INSERT INTO Fornecedores (Nome, Cidade) VALUES ("Solar Coca-Cola","Simoes Filho"); /*2*/
INSERT INTO Fornecedores (Nome, Cidade) VALUES ("Ambev","Salvador"); /*3*/
INSERT INTO Fornecedores (Nome, Cidade) VALUES ("Melbee","Rio Preto"); /*4*/

INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Doritos 25g",10,14.50);/*1*/
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Guarana Jesus 200ml",12,5.0);/*2*/
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Mel 500g",2,30.00);/*3*/
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Cheetos 25g",10,10.50);/*4*/
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Guarana Antartica 200ml",12,5.0);/*5*/
INSERT INTO Produtos (NomeProduto, Quantidade, Preco) VALUES ("Corona 500ml",12,12.50);/*6*/

INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (1,1,12,'2025-08-02');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (2,2,12,'2025-08-01');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (3,4,12,'2025-08-02');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (4,1,12,'2025-08-02');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (5,3,12,'2025-08-02');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (6,4,12,'2025-08-02');
INSERT INTO Estoque (ProdutoID,FornecedorID,Quantidade,DataEntrada) VALUES (1,1,12,'2025-08-01');

/*---------------------------------------------------------------------------*/
SELECT Fornecedores.ID, Fornecedores.Nome, Estoque.EstoqueID
FROM Fornecedores
LEFT JOIN Estoque ON Fornecedores.ID = Estoque.FornecedorID

UNION

SELECT Fornecedores.ID, Fornecedores.Nome, Estoque.EstoqueID
FROM Estoque
LEFT JOIN Fornecedores ON Estoque.FornecedorID = Fornecedores.ID;

SELECT Produtos.ProdutoID, Produtos.NomeProduto, Estoque.EstoqueID
FROM Produtos
LEFT JOIN Estoque ON Produtos.ProdutoID = Estoque.ProdutoID

UNION

SELECT Produtos.ProdutoID, Produtos.NomeProduto, Estoque.EstoqueID
FROM Estoque
LEFT JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID;
/*---------------------------------------------------------------------------*/
SELECT 
    Prod.NomeProduto AS Produto,
    Forn.Nome AS Fornecedor,
    SUM(Est.Quantidade) AS TotalEstoque,
    COUNT(Est.EstoqueID) AS Entradas,
    MAX(Est.DataEntrada) AS UltimaEntrada
FROM Estoque Est
JOIN Produtos Prod ON Est.ProdutoID = Prod.ProdutoID
JOIN Fornecedores Forn ON Est.FornecedorID = Forn.ID
GROUP BY Prod.NomeProduto, Forn.Nome;


