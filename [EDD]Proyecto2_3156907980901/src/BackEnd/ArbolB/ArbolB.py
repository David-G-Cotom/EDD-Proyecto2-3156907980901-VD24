import NodoArbolB
from ..models import Vehiculo

class ArbolB:
    def __init__(self, orden: int):
        self.__raiz: NodoArbolB = NodoArbolB(True)
        self.__orden: Vehiculo = orden



    def get_raiz(self) -> NodoArbolB:
        return self.__raiz

    def set_raiz(self, raiz: NodoArbolB) -> None:
        self.__raiz = raiz



    def get_orden(self) -> int:
        return self.__orden

    def set_orden(self, orden: int) -> None:
        self.__orden = orden



    def insertar_clave(self, vehiculo: Vehiculo) -> None:
        nodo: NodoArbolB.NodoArbolB = self.__raiz
        if (len(nodo.get_claves()) == self.__orden-1):
            # Separacion de Pagina/Nodo
            pass
        else:
            self.__insertar_vehiculo(nodo, vehiculo)



    def __insertar_vehiculo(self, raizSubArbol: NodoArbolB.NodoArbolB, nuevoVehiculo: Vehiculo.Vehiculo):
        contador: int = len(raizSubArbol.get_claves()) - 1

        if (raizSubArbol.get_is_hoja()):
            raizSubArbol.get_claves().append(None)

            while contador >= 0 and nuevoVehiculo.get_placa() < raizSubArbol.get_claves()[contador].get_placa():
                raizSubArbol.get_claves()[contador+1] = raizSubArbol.get_claves()[contador]
                contador -= 1

            raizSubArbol.get_claves()[contador+1] = nuevoVehiculo
        else:
            while contador >= 0 and nuevoVehiculo.get_placa() < raizSubArbol.get_claves()[contador].get_placa():
                contador -= 1

            if len(raizSubArbol.get_hijos()[contador].get_claves()) == self.__orden-1:
                # Separacion de Pagina/Nodo
                pass
            
            self.__insertar_vehiculo(raizSubArbol.get_hijos()[contador], nuevoVehiculo)