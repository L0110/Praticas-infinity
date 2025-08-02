USE dfs713a;

-- Alterar campo existente
ALTER TABLE Clientes MODIFY cpf VARCHAR(11);

-- Adicionar novo campo
ALTER TABLE Clientes ADD nome2 CHAR(03);

-- Renomeando um gruo existente
ALTER TABLE Clientes CHANGE COLUMN nome nome_cliente VARCHAR(200);

SELECT * FROM Clientes;
