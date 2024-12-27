from .Lista.Lista import Lista
from .Vertice import Vertice
from .Lista.NodoLista import NodoLista
from ..models.Ruta import Ruta

class ListaAdyacencia:
    def __init__(self):
        self.__lista_vertices: Lista[Vertice] = Lista()



    def get_lista_vertices(self) -> Lista:
        return self.__lista_vertices

    def set_lista_vertices(self, lista_vertices: Lista) -> None:
        self.__lista_vertices = lista_vertices



    def insertar(self, ruta: Ruta):
        origen: Vertice = Vertice(ruta.get_origen())
        destino: Vertice = Vertice(ruta.get_destino(), ruta.get_tiempo())
        resultado: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(origen)
        if resultado != None:
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)
        else:
            resultado: NodoLista = self.__lista_vertices.insertar_final(origen)
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)