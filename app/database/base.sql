CREATE TABLE diretor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nacionalidade TEXT
);

CREATE TABLE filme (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT,
    ano INTEGER,
    diretor_id INTEGER NOT NULL,
    FOREIGN KEY (diretor_id) REFERENCES diretor(id) ON DELETE CASCADE
);