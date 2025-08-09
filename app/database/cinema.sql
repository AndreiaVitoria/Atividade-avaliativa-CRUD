CREATE TABLE diretor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nacionalidade TEXT,
    data_nascimento DATE
);

CREATE TABLE filme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano_lancamento INTEGER,
    genero TEXT,
    id_diretor INTEGER NOT NULL,
    FOREIGN KEY (id_diretor) REFERENCES diretor (id) ON DELETE CASCADE
);