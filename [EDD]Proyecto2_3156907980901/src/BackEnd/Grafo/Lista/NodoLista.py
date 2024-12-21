from ..Vertice import Vertice
import NodoLista

class NodoLista:
    def __init__(self, value: Vertice):
        self.__value: Vertice = value
        self.__siguiente: NodoLista = None



    def get_value(self) -> Vertice:
        return self.__value

    def set_value(self, value: Vertice) -> None:
        self.__value = value



    def get_siguiente(self) -> NodoLista:
        return self.__siguiente

    def set_siguiente(self, siguiente: NodoLista) -> None:
        self.__siguiente = siguiente