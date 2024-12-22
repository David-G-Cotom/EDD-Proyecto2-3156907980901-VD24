from ..models.Viaje import Viaje
from .NodoListaSimple import NodoListaSimple

class NodoListaSimple:
    def __init__(self, viaje: Viaje):
        self.__siguiente: NodoListaSimple = None
        self.__viaje: Viaje = viaje




    def get_siguiente(self) -> NodoListaSimple:
        return self.__siguiente

    def set_siguiente(self, siguiente: NodoListaSimple) -> None:
        self.__siguiente = siguiente



    def get_viaje(self) -> Viaje:
        return self.__viaje
    
    def set_viaje(self, viaje: Viaje) -> None:
        self.__viaje = viaje