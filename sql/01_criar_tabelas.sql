DROP TABLE IF EXISTS reservas;
DROP TABLE IF EXISTS ambientes;

CREATE TABLE ambientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    capacidade INTEGER NOT NULL,
    possui_computadores BOOLEAN DEFAULT FALSE,
    possui_projetor BOOLEAN DEFAULT FALSE,
    observacao TEXT
);

CREATE TABLE reservas (
    id SERIAL PRIMARY KEY,
    ambiente_id INTEGER NOT NULL REFERENCES ambientes(id),
    turma VARCHAR(120) NOT NULL,
    instrutor VARCHAR(120) NOT NULL,
    unidade_curricular VARCHAR(150),
    data_reserva DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    finalidade TEXT
);