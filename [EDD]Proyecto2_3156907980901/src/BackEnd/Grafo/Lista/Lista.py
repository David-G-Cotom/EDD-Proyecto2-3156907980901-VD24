from .NodoLista import NodoLista

class Lista:
    def __init__(self):
        self.__inicio: NodoLista = None



    def get_inicio(self) -> NodoLista:
        return self.__inicio

    def set_inicio(self, inicio: NodoLista) -> None:
        self.__inicio = inicio



    '''def insertar_final(self, valor_vertice) -> NodoLista:
        nodo_aux: NodoLista = self.__inicio
        if nodo_aux == None:
            nodo_aux = NodoLista(valor_vertice)
            self.__inicio = nodo_aux
            return self.__inicio
        
        while nodo_aux.get_siguiente() != None:
            nodo_aux = nodo_aux.get_siguiente()

        nodo_aux.set_siguiente(NodoLista(valor_vertice))
        return nodo_aux.get_siguiente()'''
    


    def insertar_frente(self, valor_vertice) -> None:
        nodo_nuevo: NodoLista = NodoLista(valor_vertice)
        if self.__inicio == None:
            self.__inicio = nodo_nuevo
            return
        
        nodo_nuevo.set_siguiente(self.__inicio)
        self.__inicio = nodo_nuevo
    


    '''def eliminar_frente(self) -> NodoLista:
        nodo_inicio_aux: NodoLista = self.__inicio
        if nodo_inicio_aux != None:
            self.__inicio = nodo_inicio_aux.get_siguiente()
            return self.__inicio



    def buscar_nodo(self, valor_vertice) -> NodoLista:
        aux: NodoLista = self.__inicio
        if aux == None:
            return None
        
        while aux != None:
            if aux.get_valor_vertice().get_valor() == valor_vertice.get_valor():
                return aux
            
            aux = aux.get_siguiente()
        return None'''