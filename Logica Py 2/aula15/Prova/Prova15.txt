/* Crie uma tabela chamada Clientes com as colunas ID, 
 Nome, Idade e Cidade. Defina a coluna ID como a chave primária e 
autoincrementável.*/

CREATE DATABASE IF NOT EXISTS Infinity_db;
USE Infinity_db;

CREATE TABLE IF NOT EXISTS Clientes(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(120),
    Idade TINYINT,
    Cidade VARCHAR(60)
);

INSERT INTO Clientes (Nome,Idade,Cidade) VALUES("Ze",10,"Lauro de Freitas");
INSERT INTO Clientes (Nome,Idade,Cidade) VALUES("Jose",20,"Vitoria da Conquista");
INSERT INTO Clientes (Nome,Idade,Cidade) VALUES("Maria",15,"Porto Seguro");
INSERT INTO Clientes (Nome,Idade,Cidade) VALUES("Arlinda",8,"Cachoeira");

SELECT * FROM Clientes;