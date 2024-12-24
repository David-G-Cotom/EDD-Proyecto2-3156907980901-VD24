from .NodoListaDoble import NodoListaDoble
from ..models.Cliente import Cliente

class ListaClientes:
    def __init__(self):
        self.__inicio: NodoListaDoble = None
        self.__fin: NodoListaDoble = None



    def get_inicio(self) -> NodoListaDoble:
        return self.__inicio

    def set_inicio(self, inicio: NodoListaDoble) -> None:
        self.__inicio = inicio

    

    def get_fin(self) -> NodoListaDoble:
        return self.__fin
    
    def set_fin(self, fin: NodoListaDoble) -> None:
        self.__fin = fin



    def __insertar_inicio(self, nodo: NodoListaDoble) -> None:
        nodo.set_siguiente(self.__inicio)
        nodo.set_anterior(self.__inicio.get_anterior())
        self.__inicio.get_anterior().set_siguiente(nodo)
        self.__inicio.set_anterior(nodo)
        self.__inicio = nodo



    def __insertar_medio(self, nodo: NodoListaDoble, nodo_siguiente: NodoListaDoble) -> None:
        nodo.set_siguiente(nodo_siguiente)
        nodo.set_anterior(nodo_siguiente.get_anterior())
        nodo_siguiente.get_anterior().set_siguiente(nodo)
        nodo_siguiente.set_anterior(nodo)



    def __insertar_final(self, nodo: NodoListaDoble) -> None:
        nodo.set_anterior(self.__fin)
        nodo.set_siguiente(self.__fin.get_siguiente())
        self.__fin.get_siguiente().set_anterior(nodo)
        self.__fin.set_siguiente(nodo)
        self.__fin = nodo



    def insertar_cliente(self, cliente: Cliente) -> None:
        nodo_nuevo: NodoListaDoble = NodoListaDoble(cliente)
        if not self.is_vacia():
            nodo_aux: NodoListaDoble = self.__inicio
            if nodo_aux == self.__inicio and nodo_aux == self.__fin:
                if nodo_nuevo.get_cliente().get_dpi() > nodo_aux.get_cliente().get_dpi():
                    self.__insertar_final(nodo_nuevo)
                else:
                    self.__insertar_inicio(nodo_nuevo)
            else:
                while nodo_aux != self.__fin:
                    if nodo_nuevo.get_cliente().get_dpi() > nodo_aux.get_cliente().get_dpi() and nodo_nuevo.get_cliente().get_dpi() < nodo_aux.get_cliente().get_dpi():
                        self.__insertar_medio(nodo_nuevo, nodo_aux.get_siguiente())
                        return
                    
                    if nodo_nuevo.get_cliente().get_dpi() < nodo_aux.get_cliente().get_dpi():
                        self.__insertar_inicio(nodo_nuevo)
                        return
                    
                    nodo_aux = nodo_aux.get_siguiente()
                self.__insertar_final(nodo_nuevo)
        else:
            nodo_nuevo.set_siguiente(nodo_nuevo)
            nodo_nuevo.set_anterior(nodo_nuevo)
            self.__inicio = self.__fin = nodo_nuevo



    def recorrer_lista(self, dpi: int) -> bool:
        return True



    def is_vacia(self) -> bool:
        return self.__inicio == None