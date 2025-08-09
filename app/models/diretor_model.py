class DiretorModel:
    def __init__(self, id, nome, nacionalidade):
        self.__id = id
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    # Getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_nacionalidade(self):
        return self.__nacionalidade


    # Setters
    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade