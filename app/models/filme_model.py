class FilmeModel:
    def __init__(self, id, titulo, ano_lancamento, genero, id_autor_diretor):
        self.__id = id
        self.__titulo = titulo
        self.__ano_lancamento = ano_lancamento
        self.__genero = genero
        self.__id_autor_diretor = id_autor_diretor

    # Getters
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_ano_lancamento(self):
        return self.__ano_lancamento

    def get_genero(self):
        return self.__genero

    def get_id_autor_diretor(self):
        return self.__id_autor_diretor

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def set_genero(self, genero):
        self.__genero = genero

    def set_id_autor_diretor(self, id_autor_diretor):
        self.__id_autor_diretor = id_autor_diretor