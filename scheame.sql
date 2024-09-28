create database Littlest__PetShop

use database Littlest__PetShop



CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100)NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(100) NOT NULL,
);

CREATE TABLE endereco (
    id_endereco INT PRIMARY KEY,
    lagradouro VARCHAR(100) not null,
    numero INT not null,
    complemento char not null,
    cep VARCHAR (20) not null,
    bairro VARCHAR (30) not null,
    municipio VARCHAR(100) not null,
    UF VARCHAR(2) NOT NULL,
    PAIS VARCHAR(100) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE

);

CREATE TABLE Pet (
    id_pet INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    tipo VARCHAR(50), 
    raca VARCHAR(50),
    idade INT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Cliente(id)
);

CREATE TABLE Servico (
    id_servico INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Agendamento (
    id_agendamento INT PRIMARY KEY AUTO_INCREMENT,
    id_pet INT,
    id_servico INT,
    data_agendamento DATE NOT NULL,
    hora_agendamento TIME NOT NULL,
    status VARCHAR(50), 
    FOREIGN KEY (id_pet) REFERENCES Pet(id_pet),
    FOREIGN KEY (id_servico) REFERENCES Servico(id_servico)
);

CREATE TABLE produto(
    id INT AUTO_INCREMENT PRIMARY KEY
    nome VARCHAR (100) not null,
    descri_prod VARCHAR (255),
    valor decimal (10,2) not null,
    qtd_estoque INT not null
);

CREATE TABLE Venda (
    id_venda INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id)
);

CREATE TABLE Pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    id_venda INT,
    forma_pagamento VARCHAR(50), 
    detalhes_pagamento VARCHAR(255),
    valor_pagamento DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES Venda(id_venda)
);