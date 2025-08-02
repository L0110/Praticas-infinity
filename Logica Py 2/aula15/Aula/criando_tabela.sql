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

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Pedro", "Rua A",1,1);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Zeca", "Rua B",2,2);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Diana", "Rua C",3,6);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Sandra", "Rua D",4,3);

INSERT INTO Clientes (nome,endereco,cpf,saldo)
VALUES ("Ariel", "Rua E",5,10);

SELECT * FROM Clientes
