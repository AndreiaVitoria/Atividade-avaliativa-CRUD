from app.database.connection import get_db
from app.models.filme_model import FilmeModel

class FilmeRepository:

    def get_all_filmes(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT f.id, f.titulo, f.genero, f.ano, f.diretor_id, d.nome
            FROM filme f
            JOIN diretor d ON f.diretor_id = d.id
        """)
        rows = cursor.fetchall()
        filmes = []
        for row in rows:
            filme = FilmeModel(id=row[0], titulo=row[1], genero=row[2], ano=row[3], diretor_id=row[4])
            filme.diretor_nome = row[5]
            filmes.append(filme)
        return filmes


    def get_filme_by_id(self, filme_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT f.id, f.titulo, f.genero, f.ano, f.diretor_id, d.nome
            FROM filme f
            JOIN diretor d ON f.diretor_id = d.id
            WHERE f.id=?
        """, (filme_id,))
        row = cursor.fetchone()
        if row:
            filme = FilmeModel(id=row[0], titulo=row[1], genero=row[2], ano=row[3], diretor_id=row[4])
            filme.diretor_nome = row[5]
            return filme
        return None


    def create_filme(self, filme):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO filme(titulo, genero, ano, diretor_id) VALUES (?, ?, ?, ?)",
            (filme.get_titulo(), filme.get_genero(), filme.get_ano(), filme.get_diretor_id())
        )
        connection.commit()

    def update_filme(self, filme):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE filme SET titulo=?, genero=?, ano=?, diretor_id=? WHERE id=?",
            (filme.get_titulo(), filme.get_genero(), filme.get_ano(), filme.get_diretor_id(), filme.get_id())
        )
        connection.commit()

    def delete_filme(self, filme_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM filme WHERE id=?", (filme_id,))
        connection.commit()

    def get_filmes_by_diretor(self, diretor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM filme WHERE diretor_id = ?", (diretor_id,))
        return cursor.fetchall()  
