-- Active: 1782929575403@@sa-ma78-aejrr-daduashdiodbaso.b.aivencloud.com@25794@alleanza_immobiliare
CREATE TABLE Endereco (
    id_endereco INT AUTO_INCREMENT PRIMARY KEY,
    rua VARCHAR(150) NOT NULL,
    numero VARCHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    estado CHAR(2),
    cep VARCHAR(10)
);

CREATE TABLE Proprietario (
    id_proprietario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(20) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Corretor (
    id_corretor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    creci VARCHAR(20) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE TipoImovel (
    id_tipo_imovel INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL -- Ex: Casa, Apartamento, Terreno
);

CREATE TABLE Documento (
    id_documento INT AUTO_INCREMENT PRIMARY KEY,
    nome_documento VARCHAR(100) NOT NULL, -- Ex: Escritura, Certidão
    tipo VARCHAR(50)
);


CREATE TABLE Imovel (
    id_imovel INT AUTO_INCREMENT PRIMARY KEY,
    id_proprietario INT,
    id_tipo_imovel INT,
    id_endereco INT,
    valor_sugerido DECIMAL(12, 2),
    status VARCHAR(20) DEFAULT 'Disponível',
    FOREIGN KEY (id_proprietario) REFERENCES Proprietario(id_proprietario),
    FOREIGN KEY (id_tipo_imovel) REFERENCES TipoImovel(id_tipo_imovel),
    FOREIGN KEY (id_endereco) REFERENCES Endereco(id_endereco)
);


CREATE TABLE Visita (
    id_visita INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_corretor INT,
    id_imovel INT,
    data_visita DATETIME NOT NULL,
    observacoes TEXT,

    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_corretor) REFERENCES Corretor(id_corretor),
    FOREIGN KEY (id_imovel) REFERENCES Imovel(id_imovel),

    CONSTRAINT uc_imovel_janela_hora UNIQUE (id_imovel, data_visita),
    CONSTRAINT uc_corretor_janela_hora UNIQUE (id_corretor, data_visita)
);

CREATE TABLE Venda (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_corretor INT,
    id_imovel INT,
    data_venda DATE NOT NULL,
    valor_venda DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_corretor) REFERENCES Corretor(id_corretor),
    FOREIGN KEY (id_imovel) REFERENCES Imovel(id_imovel)
);

CREATE TABLE Aluguel (
    id_aluguel INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_corretor INT,
    id_imovel INT,
    data_inicio DATE NOT NULL,
    valor_aluguel DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_corretor) REFERENCES Corretor(id_corretor),
    FOREIGN KEY (id_imovel) REFERENCES Imovel(id_imovel)
);

CREATE TABLE Contrato (
    id_contrato INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NULL,     -- Pode ser nulo se o contrato for de aluguel
    id_aluguel INT NULL,   -- Pode ser nulo se o contrato for de venda
    data_assinatura DATE NOT NULL,
    clausulas TEXT,
    FOREIGN KEY (id_venda) REFERENCES Venda(id_venda),
    FOREIGN KEY (id_aluguel) REFERENCES Aluguel(id_aluguel)
);

CREATE TABLE Pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_contrato INT,
    valor_pago DECIMAL(10, 2) NOT NULL,
    data_pagamento DATE NOT NULL,
    forma_pagamento VARCHAR(50),
    FOREIGN KEY (id_contrato) REFERENCES Contrato(id_contrato)
);

CREATE TABLE ImovelDocumento (
    id_imovel_documento INT AUTO_INCREMENT PRIMARY KEY,
    id_imovel INT,
    id_documento INT,
    data_arquivamento DATE,
    FOREIGN KEY (id_imovel) REFERENCES Imovel(id_imovel),
    FOREIGN KEY (id_documento) REFERENCES Documento(id_documento)
);

CREATE TABLE Anuncio (
    id_anuncio INT AUTO_INCREMENT PRIMARY KEY,
    id_imovel INT,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    data_publicacao DATE,
    FOREIGN KEY (id_imovel) REFERENCES Imovel(id_imovel)
);

CREATE TABLE FotoImovel (
    id_foto INT AUTO_INCREMENT PRIMARY KEY,
    id_anuncio INT,
    url_foto VARCHAR(255) NOT NULL,
    principal BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_anuncio) REFERENCES Anuncio(id_anuncio)
);