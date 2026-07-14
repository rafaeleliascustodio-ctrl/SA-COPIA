-- ============================================
-- VIEWS - SISTEMA IMOBILIÁRIA
-- ============================================

-- 1. Imóveis disponíveis
CREATE VIEW vw_imoveis_disponiveis AS
SELECT
    i.id_imovel,
    t.descricao AS tipo_imovel,
    p.nome AS proprietario,
    i.valor_sugerido,
    i.status
FROM Imovel i
JOIN TipoImovel t
    ON i.id_tipo_imovel = t.id_tipo_imovel
JOIN Proprietario p
    ON i.id_proprietario = p.id_proprietario
WHERE i.status = 'Disponível';


-- 2. Agenda de visitas
CREATE VIEW vw_agenda_visitas AS
SELECT
    v.id_visita,
    c.nome AS cliente,
    co.nome AS corretor,
    v.data_visita,
    i.id_imovel
FROM Visita v
JOIN Cliente c
    ON v.id_cliente = c.id_cliente
JOIN Corretor co
    ON v.id_corretor = co.id_corretor
JOIN Imovel i
    ON v.id_imovel = i.id_imovel;


-- 3. Histórico de vendas
CREATE VIEW vw_historico_vendas AS
SELECT
    v.id_venda,
    c.nome AS cliente,
    co.nome AS corretor,
    v.valor_venda,
    v.data_venda
FROM Venda v
JOIN Cliente c
    ON v.id_cliente = c.id_cliente
JOIN Corretor co
    ON v.id_corretor = co.id_corretor;


-- 4. Histórico de aluguéis
CREATE VIEW vw_historico_alugueis AS
SELECT
    a.id_aluguel,
    c.nome AS cliente,
    co.nome AS corretor,
    a.valor_aluguel,
    a.data_inicio
FROM Aluguel a
JOIN Cliente c
    ON a.id_cliente = c.id_cliente
JOIN Corretor co
    ON a.id_corretor = co.id_corretor;


-- 5. Pagamentos realizados
CREATE VIEW vw_pagamentos AS
SELECT
    p.id_pagamento,
    c.id_contrato,
    p.valor_pago,
    p.data_pagamento,
    p.forma_pagamento
FROM Pagamento p
JOIN Contrato c
    ON p.id_contrato = c.id_contrato;