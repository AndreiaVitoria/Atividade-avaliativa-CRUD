from app.repository.filme_repository import FilmeRepository
from app.models.filme_model import FilmeModel
from app.repository.diretor_repository import DiretorRepository

class FilmeService:
    def __init__(self):
        self.diretor_repository = DiretorRepository()
        self.filme_repository = FilmeRepository()

    def get_all_filmes(self):
        return self.filme_repository.get_all_filmes()

    def create_filme(self, filme: FilmeModel):
        if filme.get_id() is not None:
            raise ValueError("ID do filme deve ser vazio ao criar.")
        if not filme.get_titulo():
            raise ValueError("Título do filme não pode estar vazio.")
        if len(filme.get_titulo()) < 2:
            raise ValueError("Título deve ter no mínimo 2 caracteres.")
        if any(char.isdigit() for char in filme.get_titulo()):
            raise ValueError("Título do filme não pode conter números.")
        if not filme.get_genero():
            raise ValueError("Gênero do filme não pode estar vazio.")
        if not filme.get_diretor_id():
            raise ValueError("Diretor do filme deve ser informado.")
        return self.filme_repository.create_filme(filme)

    def get_filme_by_id(self, filme_id):
        if filme_id is None:
            raise ValueError("ID do filme não pode estar vazio.")
        return self.filme_repository.get_filme_by_id(filme_id)

    def update_filme(self, filme: FilmeModel):
        if filme.get_id() is None:
            raise ValueError("ID do filme não pode estar vazio para atualização.")
        if not filme.get_titulo():
            raise ValueError("Título do filme não pode estar vazio.")
        if any(char.isdigit() for char in filme.get_titulo()):
            raise ValueError("Título do filme não pode conter números.")
        if not filme.get_genero():
            raise ValueError("Gênero do filme não pode estar vazio.")
        if not filme.get_diretor_id():
            raise ValueError("Diretor do filme deve ser informado.")

        return self.filme_repository.update_filme(filme)

    def delete_filme(self, filme_id):
        if filme_id is None:
            raise ValueError("ID do filme não pode estar vazio para exclusão.")
        return self.filme_repository.delete_filme(filme_id)
