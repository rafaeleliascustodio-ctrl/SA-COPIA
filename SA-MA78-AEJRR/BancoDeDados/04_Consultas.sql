-- 1. Listar todos os clientes cadastrados

SELECT id_cliente, nome, telefone, email
FROM Cliente
ORDER BY nome;


-- 2. Listar todos os corretores cadastrados

SELECT id_corretor, nome, creci, telefone
FROM Corretor
ORDER BY nome;


-- 3. Listar todos os imóveis juntamente com seu proprietário

SELECT i.id_imovel,
       p.nome AS proprietario,
       i.valor_sugerido,
       i.status
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
ORDER BY i.id_imovel;


-- 4. Listar imóveis disponíveis com endereço

SELECT i.id_imovel,
       e.rua,
       e.numero,
       e.bairro,
       e.cidade,
       i.valor_sugerido
FROM Imovel i
JOIN Endereco e
ON i.id_endereco = e.id_endereco
WHERE i.status = 'Disponível';


-- 5. Buscar imóveis com valor superior a R$ 500.000

SELECT id_imovel,
       valor_sugerido,
       status
FROM Imovel
WHERE valor_sugerido > 500000;


-- 6. Buscar imóveis entre R$ 200.000 e R$ 400.000

SELECT id_imovel,
       valor_sugerido,
       status
FROM Imovel
WHERE valor_sugerido BETWEEN 200000 AND 400000;


-- 7. Buscar clientes cujo nome começa com a letra A

SELECT nome,
       telefone,
       email
FROM Cliente
WHERE nome LIKE 'A%';


-- 8. Buscar imóveis disponíveis filtrando por tipo e faixa de preço

SELECT i.id_imovel,
       t.descricao AS tipo,
       i.valor_sugerido,
       e.bairro,
       e.cidade
FROM Imovel i
JOIN TipoImovel t
ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Endereco e
ON i.id_endereco = e.id_endereco
WHERE i.status = 'Disponível'
AND t.descricao = 'Apartamento'
AND i.valor_sugerido BETWEEN 300000 AND 600000;


-- 9. Contar a quantidade total de contratos cadastrados

SELECT COUNT(id_contrato) AS total_contratos
FROM Contrato;


-- 10. Contar a quantidade total de anúncios cadastrados

SELECT COUNT(id_anuncio) AS total_anuncios
FROM Anuncio;

-- 11. Calcular o valor total recebido em pagamentos

SELECT SUM(valor_pago) AS total_recebido
FROM Pagamento;


-- 12. Mostrar o menor valor de imóvel cadastrado

SELECT MIN(valor_sugerido) AS menor_valor
FROM Imovel;


-- 13. Mostrar o maior valor de imóvel cadastrado

SELECT MAX(valor_sugerido) AS maior_valor
FROM Imovel;


-- 14. Mostrar a quantidade de imóveis agrupados por status

SELECT status,
       COUNT(id_imovel) AS quantidade
FROM Imovel
GROUP BY status
ORDER BY quantidade DESC;


-- 15. Mostrar a quantidade de imóveis por cidade

SELECT e.cidade,
       COUNT(i.id_imovel) AS quantidade_imoveis
FROM Endereco e
JOIN Imovel i
ON e.id_endereco = i.id_endereco
GROUP BY e.cidade
ORDER BY quantidade_imoveis DESC;


-- 16. Mostrar a quantidade de imóveis por proprietário

SELECT p.nome AS proprietario,
       COUNT(i.id_imovel) AS quantidade_imoveis
FROM Proprietario p
JOIN Imovel i
ON p.id_proprietario = i.id_proprietario
GROUP BY p.nome
ORDER BY quantidade_imoveis DESC;


-- 17. Mostrar a média do valor dos imóveis por tipo

SELECT t.descricao AS tipo_imovel,
       ROUND(AVG(i.valor_sugerido),2) AS media_valor
FROM TipoImovel t
JOIN Imovel i
ON t.id_tipo_imovel = i.id_tipo_imovel
GROUP BY t.descricao
ORDER BY media_valor DESC;


-- 18. Mostrar a quantidade de visitas realizadas por imóvel

SELECT i.id_imovel,
       COUNT(v.id_visita) AS total_visitas
FROM Imovel i
LEFT JOIN Visita v
ON i.id_imovel = v.id_imovel
GROUP BY i.id_imovel
ORDER BY total_visitas DESC;


-- 19. Mostrar a quantidade de visitas realizadas por corretor

SELECT c.nome,
       COUNT(v.id_visita) AS total_visitas
FROM Corretor c
LEFT JOIN Visita v
ON c.id_corretor = v.id_corretor
GROUP BY c.nome
ORDER BY total_visitas DESC;


-- 20. Mostrar a quantidade de fotos cadastradas por anúncio

SELECT a.titulo,
       COUNT(f.id_foto) AS total_fotos
FROM Anuncio a
LEFT JOIN FotoImovel f
ON a.id_anuncio = f.id_anuncio
GROUP BY a.titulo
ORDER BY total_fotos DESC;

-- 21. Mostrar o valor total vendido por cada corretor

SELECT c.nome,
       COUNT(v.id_venda) AS total_vendas,
       SUM(v.valor_venda) AS valor_total_vendido
FROM Corretor c
JOIN Venda v
ON c.id_corretor = v.id_corretor
GROUP BY c.nome
ORDER BY valor_total_vendido DESC;


-- 22. Calcular a receita mensal prevista dos contratos de aluguel ativos

SELECT SUM(a.valor_aluguel) AS receita_mensal_total,
       COUNT(a.id_aluguel) AS contratos_ativos
FROM Aluguel a
JOIN Imovel i
ON a.id_imovel = i.id_imovel
WHERE i.status = 'Alugado';


-- 23. Mostrar as formas de pagamento mais utilizadas pelos clientes

SELECT forma_pagamento,
       COUNT(id_pagamento) AS quantidade_pagamentos,
       SUM(valor_pago) AS total_recebido
FROM Pagamento
GROUP BY forma_pagamento
ORDER BY quantidade_pagamentos DESC;


-- 24. Mostrar a quantidade de imóveis cadastrados por tipo

SELECT t.descricao AS tipo_imovel,
       COUNT(i.id_imovel) AS quantidade
FROM TipoImovel t
LEFT JOIN Imovel i
ON t.id_tipo_imovel = i.id_tipo_imovel
GROUP BY t.descricao
ORDER BY quantidade DESC;


-- 25. Mostrar os contratos de aluguel com a última data de pagamento

SELECT con.id_contrato,
       cli.nome AS inquilino,
       alu.valor_aluguel,
       MAX(pag.data_pagamento) AS ultimo_pagamento
FROM Contrato con
JOIN Aluguel alu
ON con.id_aluguel = alu.id_aluguel
JOIN Cliente cli
ON alu.id_cliente = cli.id_cliente
JOIN Pagamento pag
ON con.id_contrato = pag.id_contrato
GROUP BY con.id_contrato,
         cli.nome,
         alu.valor_aluguel;


-- 26. Mostrar os cinco imóveis com maior número de visitas

SELECT i.id_imovel,
       t.descricao AS tipo,
       e.bairro,
       COUNT(v.id_visita) AS total_visitas
FROM Imovel i
JOIN TipoImovel t
ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Endereco e
ON i.id_endereco = e.id_endereco
JOIN Visita v
ON i.id_imovel = v.id_imovel
GROUP BY i.id_imovel,
         t.descricao,
         e.bairro
ORDER BY total_visitas DESC
LIMIT 5;


-- 27. Selecionar clientes interessados em imóveis de uma cidade

SELECT DISTINCT c.nome,
                c.email,
                e.cidade
FROM Cliente c
JOIN Visita v
ON c.id_cliente = v.id_cliente
JOIN Imovel i
ON v.id_imovel = i.id_imovel
JOIN Endereco e
ON i.id_endereco = e.id_endereco
WHERE e.cidade = 'São Paulo';


-- 28. Listar imóveis que não possuem documentos cadastrados

SELECT i.id_imovel,
       i.status,
       p.nome AS proprietario,
       p.telefone
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
LEFT JOIN ImovelDocumento idoc
ON i.id_imovel = idoc.id_imovel
WHERE idoc.id_imovel_documento IS NULL;


-- 29. Mostrar os cinco bairros com maior média de valor dos imóveis

SELECT e.bairro,
       e.cidade,
       ROUND(AVG(i.valor_sugerido),2) AS media_preco
FROM Endereco e
JOIN Imovel i
ON e.id_endereco = i.id_endereco
GROUP BY e.bairro,
         e.cidade
ORDER BY media_preco DESC
LIMIT 5;


-- 30. Calcular o tempo médio entre a publicação do anúncio e a venda do imóvel

SELECT ROUND(AVG(DATEDIFF(v.data_venda, a.data_publicacao)),0)
AS media_dias_para_venda
FROM Anuncio a
JOIN Venda v
ON a.id_imovel = v.id_imovel;


-- 31. Auditar imóveis vendidos ou alugados sem registro correspondente

SELECT i.id_imovel,
       i.status,
       p.nome AS proprietario
FROM Imovel i
JOIN Proprietario p
ON i.id_proprietario = p.id_proprietario
WHERE i.status IN ('Vendido','Alugado')
AND i.id_imovel NOT IN
(
    SELECT id_imovel
    FROM Venda
)
AND i.id_imovel NOT IN
(
    SELECT id_imovel
    FROM Aluguel
);


-- 32. Calcular a comissão dos corretores (5% sobre as vendas)

SELECT c.id_corretor,
       c.nome,
       COUNT(v.id_venda) AS total_vendas,
       SUM(v.valor_venda) AS valor_total_vendido,
       ROUND(SUM(v.valor_venda) * 0.05,2) AS comissao
FROM Corretor c
JOIN Venda v
ON c.id_corretor = v.id_corretor
GROUP BY c.id_corretor,
         c.nome
ORDER BY comissao DESC;
