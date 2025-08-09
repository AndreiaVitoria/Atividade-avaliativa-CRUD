class FilmeModel:
    def __init__(self, id, titulo, genero, ano, diretor_id):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__ano = ano
        self.__diretor_id = diretor_id

    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero

    def get_ano(self):
        return self.__ano

    def get_diretor_id(self):
        return self.__diretor_id

    def set_id(self, id):
        self.__id = id

    def set_titulo(self, titulo):
        self.__titulo = titulo
        
    def set_genero(self, genero):
        self.__genero = genero

    def set_ano(self, ano):
        self.__ano = ano

    def set_diretor_id(self, diretor_id):
        self.__diretor_id = diretor_id
