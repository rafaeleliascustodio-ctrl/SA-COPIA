-- ============================================
-- MANIPULAÇÃO DE DADOS
-- ============================================

-- ============================================
-- INSERT
-- Cadastra um novo cliente
-- ============================================
'''
INSERT INTO Cliente (nome, cpf, telefone, email)
VALUES (
    'Marcos Vinicius',
    '55555555555',
    '48999995555',
    'marcos@email.com'
);


-- ============================================
-- UPDATE
-- Atualiza o telefone e e-mail de um cliente
-- ============================================

UPDATE Cliente
SET
    telefone = '48988887777',
    email = 'marcos.vinicius@email.com'
WHERE id_cliente = 4;


-- ============================================
-- UPDATE
-- Altera o status de um imóvel
-- ============================================

UPDATE Imovel
SET status = 'Vendido'
WHERE id_imovel = 1;


-- ============================================
-- DELETE
-- Remove uma visita cadastrada
-- ============================================

DELETE FROM Visita
WHERE id_visita = 3;


-- ============================================
-- DELETE
-- Remove um anúncio
-- ============================================

DELETE FROM Anuncio
WHERE id_anuncio = 3;
'''