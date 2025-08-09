from app.repository.diretor_repository import DiretorRepository
from app.models.diretor_model import DiretorModel
from app.repository.filme_repository import FilmeRepository

class DiretorService:
    def __init__(self):
        self.diretor_repository = DiretorRepository()
        self.filme_repository = FilmeRepository()

    def get_all_diretores(self):
        return self.diretor_repository.get_all_diretores()

    def create_diretor(self, diretor: DiretorModel):
        if diretor.get_id() is not None:
            raise ValueError("ID do diretor deve ser vazio ao criar.")
        if not diretor.get_nome():
            raise ValueError("Nome do diretor não pode estar vazio.")
        if len(diretor.get_nome()) < 2:
            raise ValueError("Nome deve ter no mínimo 2 caracteres.")
        if any(char.isdigit() for char in diretor.get_nome()):
            raise ValueError("Nome do diretor não pode conter números.")
        if not diretor.get_nacionalidade():
            raise ValueError("Nacionalidade do diretor não pode estar vazia.")
        return self.diretor_repository.create_diretor(diretor)

    def get_diretor_by_id(self, diretor_id):
        if diretor_id is None:
            raise ValueError("ID do diretor não pode estar vazio.")
        return self.diretor_repository.get_diretor_by_id(diretor_id)

    def update_diretor(self, diretor: DiretorModel):
        if diretor.get_id() is None:
            raise ValueError("ID do diretor não pode estar vazio para atualização.")
        if len(diretor.get_nome()) < 2:
            raise ValueError("Nome deve ter no mínimo 2 caracteres.")
        if not diretor.get_nome():
            raise ValueError("Nome do diretor não pode estar vazio.")
        if any(char.isdigit() for char in diretor.get_nome()):
            raise ValueError("Nome do diretor não pode conter números.")
        if not diretor.get_nacionalidade():
            raise ValueError("Nacionalidade do diretor não pode estar vazia.")

        return self.diretor_repository.update_diretor(diretor)

    def delete_diretor(self, diretor_id):
        if diretor_id is None:
            raise ValueError("ID do diretor não pode estar vazio para exclusão.")
        filmes = self.filme_repository.get_filmes_by_diretor(diretor_id)
        if filmes:
            raise ValueError("Não é possível excluir um diretor que possui filmes associados.")
        return self.diretor_repository.delete_diretor(diretor_id)
