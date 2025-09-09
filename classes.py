class Item:
    def __init__(self, codigo, titulo, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel

class Filme(Item):
    pass

class Jogo(Item):
    pass

class Cliente:
    pass

class Locadora:
    pass
        