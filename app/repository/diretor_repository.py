from app.database.connection import get_db
from app.models.diretor_model import DiretorModel

class DiretorRepository:

    def get_all_diretores(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM diretor")
        rows = cursor.fetchall()
        return [
            DiretorModel(
                id=row[0],
                nome=row[1],
                nacionalidade=row[2],
            )
            for row in rows
        ]

    def get_diretor_by_id(self, diretor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM diretor WHERE id=?", (diretor_id,))
        row = cursor.fetchone()
        return DiretorModel(
            id=row[0],
            nome=row[1],
            nacionalidade=row[2],
        ) if row else None

    def create_diretor(self, diretor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO diretor(nome, nacionalidade) VALUES (?, ?)",
            (diretor.get_nome(), diretor.get_nacionalidade())
        )
        connection.commit()

    def update_diretor(self, diretor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE diretor SET nome=?, nacionalidade=? WHERE id=?",
            (diretor.get_nome(), diretor.get_nacionalidade(), diretor.get_id())
        )
        connection.commit()

    def delete_diretor(self, diretor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM diretor WHERE id=?", (diretor_id,))
        connection.commit()
