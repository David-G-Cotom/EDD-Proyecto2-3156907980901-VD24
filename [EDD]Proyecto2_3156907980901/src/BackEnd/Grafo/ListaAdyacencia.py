from Lista.Lista import Lista
from Vertice import Vertice
from Lista.NodoLista import NodoLista

class ListaAdyacencia:
    def __init__(self):
        self.__lista_vertices: Lista = Lista()



    def get_lista_vertices(self) -> Lista:
        return self.__lista_vertices

    def set_lista_vertices(self, lista_vertices: Lista) -> None:
        self.__lista_vertices = lista_vertices



    def insertar(self, origen: Vertice, destino: Vertice):
        resultado: NodoLista = self.__lista_vertices.buscar_vertice(origen)
        if resultado != None:
            resultado.get_value().get_vecinos().insertar_final(destino)
        else:
            resultado: NodoLista = self.__lista_vertices.insertar_final(origen)
            resultado.get_value().get_vecinos().insertar_final(destino)