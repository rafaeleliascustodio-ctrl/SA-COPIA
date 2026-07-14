-- ============================================
-- USUÁRIOS, ROLES E PERMISSÕES
-- ============================================

-- ============================================
-- CRIAÇÃO DOS USUÁRIOS
-- ============================================

CREATE USER 'master_imobiliaria'@'%' IDENTIFIED BY 'Master@123';
CREATE USER 'corretor1'@'%' IDENTIFIED BY 'Corretor@123';
CREATE USER 'financeiro1'@'%' IDENTIFIED BY 'Financeiro@123';

-- ============================================
-- CRIAÇÃO DAS ROLES
-- ============================================

CREATE ROLE 'role_master';
CREATE ROLE 'role_corretor';
CREATE ROLE 'role_financeiro';

-- ============================================
-- PERMISSÕES DA ROLE MASTER
-- ============================================

GRANT ALL PRIVILEGES
ON alleanza_immobiliare.*
TO 'role_master';

-- ============================================
-- PERMISSÕES DA ROLE CORRETOR
-- ============================================

GRANT SELECT, INSERT, UPDATE
ON alleanza_immobiliare.Cliente
TO 'role_corretor';

GRANT SELECT
ON alleanza_immobiliare.Imovel
TO 'role_corretor';

GRANT SELECT, INSERT
ON alleanza_immobiliare.Visita
TO 'role_corretor';

GRANT SELECT
ON alleanza_immobiliare.Anuncio
TO 'role_corretor';

-- ============================================
-- PERMISSÕES DA ROLE FINANCEIRO
-- ============================================

GRANT SELECT, INSERT, UPDATE
ON alleanza_immobiliare.Pagamento
TO 'role_financeiro';

GRANT SELECT
ON alleanza_immobiliare.Contrato
TO 'role_financeiro';

GRANT SELECT
ON alleanza_immobiliare.Venda
TO 'role_financeiro';

GRANT SELECT
ON alleanza_immobiliare.Aluguel
TO 'role_financeiro';

-- ============================================
-- ASSOCIANDO ROLES AOS USUÁRIOS
-- ============================================

GRANT 'role_master' TO 'master_imobiliaria'@'%';
GRANT 'role_corretor' TO 'corretor1'@'%';
GRANT 'role_financeiro' TO 'financeiro1'@'%';

-- ============================================
-- DEFININDO A ROLE PADRÃO
-- ============================================

SET DEFAULT ROLE 'role_master'
TO 'master_imobiliaria'@'%';

SET DEFAULT ROLE 'role_corretor'
TO 'corretor1'@'%';

SET DEFAULT ROLE 'role_financeiro'
TO 'financeiro1'@'%';

-- ============================================
-- EXEMPLO DE REVOKE
-- ============================================

REVOKE UPDATE
ON alleanza_immobiliare.Cliente
FROM 'role_corretor';

FLUSH PRIVILEGES;