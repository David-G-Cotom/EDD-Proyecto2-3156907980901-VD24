#from ..Lista.Lista import Lista
#from ..Lista.NodoLista import NodoLista
from .NodoCola import NodoCola
from ..Vertice import Vertice

class Cola:#(Lista)
    def __init__(self):
        #super().__init__()
        self.__inicio: NodoCola = None



    def get_inicio(self):
        return self.__inicio
    
    def set_inicio(self, inicio: NodoCola) -> None:
        self.__inicio = inicio



    def encolar(self, valor: Vertice) -> None:
        #Lista.insertar_final(self, valor)
        nuevo_nodo : NodoCola = NodoCola(valor)
        if self.__is_vacia():
            self.__inicio = nuevo_nodo
            return
        
        nodo_aux: NodoCola = self.__inicio
        while nodo_aux.get_siguiente() != None:
            nodo_aux = nodo_aux.get_siguiente()

        nodo_aux.set_siguiente(nuevo_nodo)



    def des_encolar(self) -> NodoCola:#NodoLista:
        #return Lista.eliminar_frente(self)
        if self.__is_vacia():
            print("NO HAY ITEM EN LA COLA")
            return
        
        nodo_aux: NodoCola = self.__inicio
        self.__inicio = nodo_aux.get_siguiente()
        return nodo_aux
    


    def ordenar(self) -> None:
        if self.__is_vacia():
            print("NO HAY NADA QUE ORDENAR")
            return
        
        nodo_actual: NodoCola[Vertice] = self.__inicio
        while nodo_actual != None:
            nodo_siguiente: NodoCola[Vertice] = nodo_actual.get_siguiente()
            while nodo_siguiente != None:
                if nodo_actual.get_valor_vertice().get_peso_acumulado() > nodo_siguiente.get_valor_vertice().get_peso_acumulado():
                    vertice_aux: Vertice = nodo_siguiente.get_valor_vertice()
                    nodo_siguiente.set_valor_vertice(nodo_actual.get_valor_vertice())
                    nodo_actual.set_valor_vertice(vertice_aux)

                nodo_siguiente = nodo_siguiente.get_siguiente()
            nodo_actual = nodo_actual.get_siguiente()


    
    def buscar(self, valor: str) -> NodoCola:
        nodo_aux: NodoCola[Vertice] = self.__inicio
        while nodo_aux != None:
            if nodo_aux.get_valor_vertice().get_valor() == valor:
                return nodo_aux
            
            nodo_aux = nodo_aux.get_siguiente()
        return None
    


    def __is_vacia(self) -> bool:
        return self.__inicio == None