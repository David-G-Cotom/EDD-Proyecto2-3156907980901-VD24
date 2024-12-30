class NodoCola:
    def __init__(self, valor_vertice):
        from ..Vertice import Vertice
        self.__valor_vertice: Vertice = valor_vertice
        self.__siguiente: NodoCola = None



    def get_valor_vertice(self):
        return self.__valor_vertice

    def set_valor_vertice(self, valor_vertice) -> None:
        self.__valor_vertice = valor_vertice



    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente) -> None:
        self.__siguiente = siguiente