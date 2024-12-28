from .Lista.Lista import Lista
from .Cola.Cola import Cola
from .Vertice import Vertice
from .Lista.NodoLista import NodoLista
from ..models.Ruta import Ruta

class ListaAdyacencia:
    def __init__(self):
        self.__lista_vertices: Lista[Vertice] = Lista()
        self.__ruta_corta: Lista[Vertice] = Lista()



    def get_lista_vertices(self) -> Lista:
        return self.__lista_vertices

    def set_lista_vertices(self, lista_vertices: Lista) -> None:
        self.__lista_vertices = lista_vertices



    def get_ruta_corta(self) -> Lista:
        return self.__ruta_corta

    def set_ruta_corta(self, ruta_corta: Lista) -> None:
        self.__ruta_corta = ruta_corta



    def insertar(self, ruta: Ruta):
        origen: Vertice = Vertice(ruta.get_origen())
        destino: Vertice = Vertice(ruta.get_destino(), ruta.get_tiempo())
        resultado: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(origen)
        if resultado != None:
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)
        else:
            resultado: NodoLista = self.__lista_vertices.insertar_final(origen)
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)



    def obtener_ruta_corta(self, origen: str, destino: str):
        cola_ruta: Cola = Cola()
        nodo_origen: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(Vertice(origen))
        cola_ruta.encolar(nodo_origen.get_valor_vertice())
        self.__obtener_ruta_corta_recursiva(Vertice(destino), cola_ruta)



    def __obtener_ruta_corta_recursiva(self, destino: Vertice, cola_ruta: Cola):
        nodo_origen: NodoLista[Vertice] = cola_ruta.des_encolar()
        if nodo_origen == None:
            print("LA CIUDAD DE ORIGEN NO EXISTE")
            return
        
        nodo_origen = self.__lista_vertices.buscar_nodo(nodo_origen.get_valor_vertice())
        self.__ruta_corta.insertar_final(nodo_origen)
        nodo_origen.get_valor_vertice().set_is_visitado(True)
        if nodo_origen.get_valor_vertice().get_valor() == destino.get_valor():
            # ENCONTRAMOS EL ULTIMO NODO
            return
        
        inicio_vecinos: NodoLista[Vertice] = nodo_origen.get_valor_vertice().get_vecinos().get_inicio()
        while inicio_vecinos != None:
            nodo_vecino: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(inicio_vecinos.get_valor_vertice())
            if not nodo_vecino.get_valor_vertice().get_is_visitado():
                nodo_vecino.get_valor_vertice().actualizar_peso_acumulado(inicio_vecinos.get_valor_vertice().get_peso())
                cola_ruta.encolar(nodo_vecino.get_valor_vertice())
        
            inicio_vecinos = inicio_vecinos.get_siguiente()
        self.ordenar_cola(cola_ruta)
        self.__obtener_ruta_corta_recursiva(destino, cola_ruta)

        

    def ordenar_cola(self, cola: Cola) -> None:
        inicio: NodoLista = cola.get_inicio()
        vertice_aux: Vertice = None
        while inicio != None:
            inicio_siguiente = inicio.get_siguiente()
            while inicio_siguiente != None:
                if inicio.get_valor_vertice().get_peso_acumulado() > inicio_siguiente.get_valor_vertice().get_peso_acumulado():
                    vertice_aux = inicio_siguiente.get_valor_vertice()
                    inicio_siguiente.set_valor_vertice(inicio.get_valor_vertice())
                    inicio.set_valor_vertice(vertice_aux)

                inicio_siguiente = inicio_siguiente.get_siguiente()
            inicio = inicio.get_siguiente()