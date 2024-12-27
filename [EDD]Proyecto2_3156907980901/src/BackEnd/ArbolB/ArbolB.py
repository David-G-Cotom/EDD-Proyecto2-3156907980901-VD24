from .NodoArbolB import NodoArbolB
from ..models.Vehiculo import Vehiculo
from tkinter import messagebox

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
            print("NUEVO VEHICULO REGISTRADO!!!")
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



    def eliminar_vehiculo(self, nodo: NodoArbolB, vehiculo: Vehiculo) -> None:
        i: int = 0
        while i<len(nodo.get_claves()) and vehiculo.get_placa()>nodo.get_claves()[i].get_placa():
            i += 1

        if nodo.get_is_hoja():
            # EL VEHICULO ESTA EN UN NODO HOJA
            if i<len(nodo.get_claves()) and nodo.get_claves()[i].get_placa()==vehiculo.get_placa():
                nodo.get_claves().pop(i)
                messagebox.showinfo("EXITO!!!", "Vehiculo ELiminado Exitosamente")
                return
        else:
            # EL VEHICULO ESTA EN UN NODO INTERNO
            if i<len(nodo.get_claves()) and nodo.get_claves()[i].get_placa()==vehiculo.get_placa():
                return self.__eliminar_nodo_interno(nodo, vehiculo, i)
            # EL VEHICULO NO ESTA EN EL NODO, VAMOS AL NODO HIJO
            if len(nodo.get_hijos()[i].get_claves()) < self.__orden:
                self.__rellenar_nodo(nodo, i)

            self.eliminar_vehiculo(nodo.get_hijos()[i], vehiculo)



    def __eliminar_nodo_interno(self, raiz_sub_arbol: NodoArbolB, vehiculo: Vehiculo, posicion: int) -> None:
        # EL HIJO IZQUIERDO DEL NODO ACTUAL YA TIENE EL NUMERO MAXIMO DE CLAVES
        if len(raiz_sub_arbol.get_hijos()[posicion].get_claves()) >= self.__orden:
            clave_anterior: Vehiculo = self.__get_clave_anterior(raiz_sub_arbol, posicion)
            raiz_sub_arbol.get_claves()[posicion] = clave_anterior
            self.eliminar_vehiculo(raiz_sub_arbol.get_hijos()[posicion], clave_anterior)
        # EL HIJO DERECHO DEL NODO ACTUAL YA TIENE EL NUMERO MAXIMO DE CLAVES
        elif len(raiz_sub_arbol.get_hijos()[posicion + 1].get_claves()) >= self.__orden:
            clave_siguiente: Vehiculo = self.__get_clave_siguiente(raiz_sub_arbol, posicion)
            raiz_sub_arbol.get_claves()[posicion] = clave_siguiente
            self.eliminar_vehiculo(raiz_sub_arbol.get_hijos()[posicion + 1], clave_siguiente)
        # AMBOS HIJOS TIENEN MENOS DE self.__orden (5) CLAVES
        else:
            self.__unir_hijos(raiz_sub_arbol, posicion)
            self.eliminar_vehiculo(raiz_sub_arbol.get_hijos()[posicion], vehiculo)



    def __get_clave_anterior(self, nodo: NodoArbolB, posicion: int) -> Vehiculo:
        nodo_hijo: NodoArbolB = nodo.get_hijos()[posicion]
        while not nodo_hijo.get_is_hoja():
            nodo_hijo = nodo_hijo.get_hijos()[len(nodo_hijo.get_hijos()) - 1]

        return nodo_hijo.get_claves()[len(nodo_hijo.get_claves) - 1]



    def __get_clave_siguiente(self, nodo: NodoArbolB, posicion: int) -> Vehiculo:
        nodo_hijo: NodoArbolB = nodo.get_hijos()[posicion + 1]
        while not nodo_hijo.get_is_hoja():
            nodo_hijo = nodo_hijo.get_hijos()[0]

        return nodo_hijo.get_claves()[0]
    


    def __unir_hijos(self, raiz_sub_arbol: NodoArbolB, posicion: int) -> None:
        hijo_izquierdo: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion]
        hijo_derecho: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion + 1] 
        hijo_izquierdo.get_claves().append(raiz_sub_arbol.get_claves()[posicion])
        hijo_izquierdo.get_claves().extend(hijo_derecho.get_claves())
        if not hijo_izquierdo.get_is_hoja():
            hijo_izquierdo.get_hijos().extend(hijo_derecho.get_hijos())
        # SE ELIMINAR LA CLAVE Y EL HIJO DERECHO A ESA CLAVE DEL NODO RAIZ
        raiz_sub_arbol.get_claves().pop(posicion)
        raiz_sub_arbol.get_hijos().pop(posicion + 1)
        # SI EL NODO RAIZ SE QUEDA VACIA, SE REDUCE LA ALTURA DEL ARBOL
        if len(raiz_sub_arbol.get_claves()) == 0:
            self.__raiz = hijo_izquierdo



    def __rellenar_nodo(self, nodo: NodoArbolB, posicion: int) -> None:
        if posicion!=0 and len(nodo.get_hijos()[posicion - 1].get_claves())>=self.__orden:
            self.__prestar_clave_de_anterior(nodo, posicion)
        elif posicion!=len(nodo.get_hijos())-1 and len(nodo.get_hijos()[posicion+1].get_claves())>=self.__orden:
            self.__prestar_clave_de_siguiente(nodo, posicion)
        else:
            if posicion != len(nodo.get_hijos())-1:
                self.__unir_hijos(nodo, posicion)
            else:
                self.__unir_hijos(nodo, posicion - 1)



    def __prestar_clave_de_anterior(sef, raiz_sub_arbol: NodoArbolB, posicion: int) -> None:
        hijo_izquierdo: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion]
        hijo_derecho: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion - 1]
        # MOVER LA ULTIMA CLAVE DEL HIJO DERECHO AL NODO RAIZ
        hijo_izquierdo.get_claves().insert(0, raiz_sub_arbol.get_claves()[posicion - 1])
        raiz_sub_arbol.get_claves()[posicion - 1] = hijo_derecho.get_claves().pop()
        # MOVER EL ULTIMO HIJO DEL HIJO DERECHO AL HIJO IZQUIERDO SI EL HIJO DERECHO NO ES UNA HOJA
        if not hijo_izquierdo.get_is_hoja():
            hijo_izquierdo.get_hijos().insert(0, hijo_derecho.get_hijos().pop())



    def __prestar_clave_de_siguiente(self, raiz_sub_arbol: NodoArbolB, posicion: int) -> None:
        hijo_izquierdo: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion]
        hijo_derecho: NodoArbolB = raiz_sub_arbol.get_hijos()[posicion + 1]
        # MOVER LA PRIMERA CLAVE DEL HIJO DERECHO AL NODO RAIZ
        hijo_izquierdo.get_claves().append(raiz_sub_arbol.get_claves()[posicion])
        raiz_sub_arbol.get_claves()[posicion] = hijo_derecho.get_claves().pop(0)
        # MOVER EL PRIMER HIJO DEL HIJO DERECHO AL HIJO IZQUIERDO SI EL HIJO DERECHO NO ES UNA HOJA
        if not hijo_izquierdo.get_is_hoja():
            hijo_izquierdo.get_hijos().append(hijo_derecho.get_hijos().pop(0))



    def modificar_vehiculo(self, placa: str):
        pass



    def __buscar_vehiculo(self, nodo: NodoArbolB, placa: str) -> Vehiculo:
        i: int = 0
        while i < self.__orden-1 and nodo.get_claves()[i].get_placa() < placa:
            i += 1

        if i < self.__orden-1 and nodo.get_claves()[i].get_placa() == placa:
            return nodo.get_claves()[i]
        
        if nodo.get_is_hoja():
            return None
        
        self.__buscar_vehiculo(nodo.get_hijos()[i], placa)



    def __recorrer_arbol(self) -> None:
        pass