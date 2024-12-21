from ..models.Vehiculo import Vehiculo
import NodoArbolB

class NodoArbolB:
    def __init__(self, is_hoja: bool = False):
        self.__is_hoja: bool = is_hoja
        self.__claves: list[Vehiculo] = []  # (m - 1)      m=orden_arbol
        self.__hijos: list[NodoArbolB] = []   # m     m=orden_arbol



    def get_is_hoja(self) -> bool:
        return self.__is_hoja

    def set_is_hoja(self, is_hoja: bool) -> None:
        self.__is_hoja = is_hoja



    def get_claves(self) -> list[Vehiculo]:
        return self.__claves

    def set_calves(self, claves: list[Vehiculo]) -> None:
        self.__claves = claves



    def get_hijos(self) -> list[NodoArbolB]:
        return self.__hijos

    def set_hijos(self, hijos: list[NodoArbolB]) -> None:
        self.__hijos = hijos