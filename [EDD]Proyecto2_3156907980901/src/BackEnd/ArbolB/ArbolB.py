from NodoArbolB import NodoArbolB
from ..models.Vehiculo import Vehiculo

class ArbolB:
    def __init__(self, orden: int):
        self.__raiz: NodoArbolB = NodoArbolB(True)
        self.__orden: int = orden



    def get_raiz(self) -> NodoArbolB:
        return self.__raiz

    def set_raiz(self, raiz: NodoArbolB) -> None:
        self.__raiz = raiz



    def get_orden(self) -> int:
        return self.__orden

    def set_orden(self, orden: int) -> None:
        self.__orden = orden



    def insertar_vehiculo(self, nuevo_vehiculo: Vehiculo) -> None:
        nodo_raiz: NodoArbolB = self.__raiz
        self.__insertar_vehiculo_no_completo(nodo_raiz, nuevo_vehiculo)
        if len(nodo_raiz.get_claves()) > self.__orden-1:
            nodo_aux: NodoArbolB = NodoArbolB()
            self.__raiz = nodo_aux
            nodo_aux.get_hijos().insert(0, nodo_raiz)
            self.__dividir_pagina(nodo_aux, 0)



    def __insertar_vehiculo_no_completo(self, raiz_sub_arbol: NodoArbolB, nuevo_vehiculo: Vehiculo):
        posicion: int = len(raiz_sub_arbol.get_claves()) - 1
        if raiz_sub_arbol.get_is_hoja():
            raiz_sub_arbol.get_claves().append(None)
            while posicion >= 0 and nuevo_vehiculo.get_placa() < raiz_sub_arbol.get_claves()[posicion].get_placa():
                raiz_sub_arbol.get_claves()[posicion + 1] = raiz_sub_arbol.get_claves()[posicion]
                posicion -= 1

            raiz_sub_arbol.get_claves()[posicion + 1] = nuevo_vehiculo
        else:
            while posicion >= 0 and nuevo_vehiculo.get_placa() < raiz_sub_arbol.get_claves()[posicion].get_placa():
                posicion -= 1

            posicion += 1
            self.__insertar_vehiculo_no_completo(raiz_sub_arbol.get_hijos()[posicion], nuevo_vehiculo)
            if len(raiz_sub_arbol.get_hijos()[posicion].get_claves()) > self.__orden-1:
                # Separacion de Pagina/Nodo
                self.__dividir_pagina(raiz_sub_arbol, posicion)



    def __dividir_pagina(self, raiz_sub_arbol: NodoArbolB, posicion: int):
        posicion_media: int = int((self.__orden-1) / 2) # En este caso es de Orden 5 (impar), caso contrario (par) solo se divide en 2
        hijo: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion]
        nodo: NodoArbolB = NodoArbolB(hijo.get_is_hoja())
        raiz_sub_arbol.get_hijos().insert(posicion + 1, nodo)
        raiz_sub_arbol.get_claves().insert(posicion, hijo.get_claves()[posicion_media])
        nodo.set_calves(hijo.get_claves()[posicion_media + 1: (posicion_media*2) + 1])
        hijo.set_calves(hijo.get_claves()[0 : posicion_media])
        if not hijo.get_is_hoja():
            nodo.set_hijos(hijo.get_hijos()[posicion_media + 1: (posicion_media*2) + 2])
            hijo.set_hijos(hijo.get_hijos()[0 : posicion_media + 1])