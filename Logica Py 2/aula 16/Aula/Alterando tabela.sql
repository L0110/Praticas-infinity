USE dfs713a;
-- Usando "_" no nome, o script terá preferencia de uso
-- Alterar campo existente
ALTER TABLE Clientes MODIFY cpf VARCHAR(11);

-- Adicionar novo campo
ALTER TABLE Clientes ADD nome2 CHAR(03);
ALTER TABLE Produtos ADD CHECK (preco >= 0);

-- Renomeando um gruo existente
ALTER TABLE Clientes CHANGE COLUMN nome nome_cliente VARCHAR(200);

-- ATUALIZACAO
UPDATE Clientes SET endereco="Travessa ABC" WHERE codigo = 1;

-- EXCLUSAO
DELETE FROM Clientes WHERE (Codigo = 4);
ALTER TABLE Clientes DROP COLUMN nome2;

-- LISTAGEM
SELECT * FROM Clientes;
SELECT * FROM Produtos;

-- AGRUAMENTO
SELECT sum(codigo),endereco
FROM Clientes
GROUP BY endereco
ORDER BY endereco;

-- BASICO
SELECT * FROM Clientes WHERE saldo>=4;
SELECT * FROM Clientes WHERE endereco LIKE"Travessa%";
-- SELECT * FROM Clientes WHERE endereco LIKE"%Travessa";
-- SELECT * FROM Clientes WHERE endereco LIKE"%Travessa%";

SELECT nome FROM Clientes WHERE nome like "%J%"