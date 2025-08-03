CREATE DATABASE IF NOT EXISTS dfs713a;
USE dfs713a;

CREATE TABLE IF NOT EXISTS Clientes(
	codigo INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255),
    email VARCHAR(255),
    cpf INT UNIQUE,
    saldo REAL CHECK (saldo >= 0)
);

-- Para associar duas tabelas, o nome da coluna pode ser diferente, mas o tipo e proppriedades de entrada recisam ser iguais
CREATE TABLE IF NOT EXISTS Pedidos(
-- REMOVER PROPRIEDADE CHAVE PRIMARIA
	cod_pedido INTEGER PRIMARY KEY,
    cod_cliente Integer,
    cod_produto integer,
    FOREIGN KEY (cod_cliente) REFERENCES Clientes(codigo),
	-- Caso haja mais de uma chave, o comando abaixo pode ser udado:
    -- PRIMARY KEY (cod_pedido, cod_cliente)
    FOREIGN KEY (cod_produto) REFERENCES Produtos(id_roduto)
);

CREATE TABLE Produtos(
	id_produto INTEGER PRIMARY KEY,
    nome_produto VARCHAR(225),
    tipo VARCHAR(255),
    preco REAL CHECK (preco >= 0)
);

-- ENTRADAS TABELA Clientes _________________________________________________________________________

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Pedro", "Rua A",1,1);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Zeca", "Rua B",2,2);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Diana", "Rua C",3,6);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Sandra", "Rua D",4,3);

INSERT INTO Clientes (nome_cliente,endereco,cpf,saldo)
VALUES ("Ariel", "Rua E",5,10);

INSERT INTO Clientes (nome_cliente,endereco,cpf,saldo)
VALUES ("Ariel", "Rua E",6,10);

INSERT INTO Clientes (nome_cliente,endereco,cpf,saldo)
VALUES ("Pedro Henrique", "Rua B",9,11);

SELECT * FROM Clientes

-- ENTRADAS TABELA PEdidos ___________________________________________________________________




