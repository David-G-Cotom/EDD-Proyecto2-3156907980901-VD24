from NodoLista import NodoLista
from ..Vertice import Vertice

class Lista:
    def __init__(self):
        self.__inicio: NodoLista = None



    def get_inicio(self) -> NodoLista:
        return self.__inicio

    def set_inicio(self, inicio: NodoLista) -> None:
        self.__inicio = inicio



    def insertar_final(self, value: Vertice) -> NodoLista:
        aux: NodoLista = self.__inicio
        if aux == None:
            aux = NodoLista(value)
            self.__inicio = aux
            return self.__inicio
        
        while aux.get_siguiente() != None:
            aux = aux.get_siguiente()

        aux.get_siguiente() = NodoLista(value)
        return aux.get_siguiente()



    def buscar_vertice(self, value: Vertice) -> NodoLista:
        aux: NodoLista = self.__inicio
        if aux == None:
            return None
        
        while aux != None:
            if aux.get_value().get_value() == value.get_value():
                return aux
            
            aux = aux.get_siguiente()
        return None