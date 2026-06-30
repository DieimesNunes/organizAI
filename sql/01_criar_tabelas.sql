CREATE TABLE ambientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    capacidade INTEGER NOT NULL,
    possui_computadores BOOLEAN DEFAULT FALSE,
    possui_projetor BOOLEAN DEFAULT FALSE,
    observacao TEXT
);

CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    ambiente_id INTEGER REFERENCES ambientes(id),
    turma VARCHAR(100) NOT NULL,
    instrutor VARCHAR(100) NOT NULL,
    unidade_curricular VARCHAR(150),
    data_reserva DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    finalidade TEXT
);

CREATE TABLE ocorrencias (
    id SERIAL PRIMARY KEY,
    ambiente_id INTEGER REFERENCES ambientes(id),
    data_ocorrencia DATE NOT NULL,
    descricao TEXT NOT NULL,
    status VARCHAR(30) DEFAULT 'Aberta'
);