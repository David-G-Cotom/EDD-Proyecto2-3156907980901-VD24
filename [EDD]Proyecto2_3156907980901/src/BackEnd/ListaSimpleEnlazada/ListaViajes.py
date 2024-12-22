from .NodoListaSimple import NodoListaSimple
from ..models.Viaje import Viaje

class ListaViaje:
    def __init__(self):
        self.__inicio: NodoListaSimple = None
        self.__fin: NodoListaSimple = None



    def get_inicio(self) -> NodoListaSimple:
        return self.__inicio

    def set_inicio(self, inicio: NodoListaSimple) -> None:
        self.__inicio = inicio

    

    def get_fin(self) -> NodoListaSimple:
        return self.__fin
    
    def set_fin(self, fin: NodoListaSimple) -> None:
        self.__fin = fin
    
    
    
    def insertar_cliente(self, viaje: Viaje) -> None:
        nodo_nuevo: NodoListaSimple = NodoListaSimple(viaje)
        if not self.is_vacia():
            self.__fin.set_siguiente(nodo_nuevo)
            self.__fin = nodo_nuevo
        else:
            self.__inicio = self.__fin = nodo_nuevo
    
    
    
    def recorrer_lista(self, id: int) -> bool:
        return True



    def is_vacia(self) -> bool:
        return self.__inicio == None