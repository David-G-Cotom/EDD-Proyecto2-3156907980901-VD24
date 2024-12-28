from ..Lista.Lista import Lista
from ..Lista.NodoLista import NodoLista

class Cola(Lista):
    def __init__(self):
        super().__init__()



    def encolar(self, valor):
        Lista.insertar_final(self, valor)



    def des_encolar(self) -> NodoLista:
        return Lista.eliminar_frente(self)