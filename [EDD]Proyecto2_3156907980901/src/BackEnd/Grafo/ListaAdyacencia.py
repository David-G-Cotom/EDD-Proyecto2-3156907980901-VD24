from .Lista.Lista import Lista
from .Cola.Cola import Cola
from .Vertice import Vertice
from .Lista.NodoLista import NodoLista
from ..models.Ruta import Ruta
from .Cola.NodoCola import NodoCola
from copy import copy

class ListaAdyacencia:
    def __init__(self):
        self.__lista_vertices: Lista[Vertice] = Lista()
        #self.__ruta_corta: Lista[Vertice] = Lista()



    def get_lista_vertices(self) -> Lista:
        return self.__lista_vertices

    def set_lista_vertices(self, lista_vertices: Lista) -> None:
        self.__lista_vertices = lista_vertices



    def get_ruta_corta(self) -> Lista:
        return self.__ruta_corta

    def set_ruta_corta(self, ruta_corta: Lista) -> None:
        self.__ruta_corta = ruta_corta



    def insertar(self, ruta: Ruta) -> None:
        nuevo_vertice: Vertice = self.__buscar_vertice(ruta.get_origen())
        if nuevo_vertice != None:
            nuevo_vertice.agregar_vecino(ruta.get_destino(), ruta.get_tiempo())
            return
        
        nuevo_vertice: Vertice = Vertice(ruta.get_origen())
        nuevo_vertice.agregar_vecino(ruta.get_destino(), ruta.get_tiempo())
        self.__lista_vertices.insertar_frente(nuevo_vertice)

        '''destino: Vertice = Vertice(ruta.get_destino(), ruta.get_tiempo())
        resultado: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(origen)
        if resultado != None:
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)
        else:
            resultado: NodoLista = self.__lista_vertices.insertar_final(origen)
            resultado.get_valor_vertice().get_vecinos().insertar_final(destino)'''



    def obtener_ruta_corta(self, origen: str, destino: str) -> Lista:
        ruta_corta: Lista[Vertice] = Lista()
        nodos_cola_visitada: Cola = Cola()
        nodos_vecinos: Cola = Cola()
        vertice_origen: Vertice = copy(self.__buscar_vertice(origen))
        if vertice_origen == None:
            print(f"LA CIUDAD {origen} NO EXISE LA CIUDAD")
            return
        
        nodos_vecinos.encolar(vertice_origen)
        resultado: Vertice = self.__obtener_ruta_corta_recursiva(destino, nodos_cola_visitada, nodos_vecinos)
        while resultado != None:
            ruta_corta.insertar_frente(resultado)
            resultado = resultado.get_padre()

        return ruta_corta
        '''cola_ruta: Cola = Cola()
        nodo_origen: NodoLista[Vertice] = self.__lista_vertices.buscar_nodo(Vertice(origen))
        cola_ruta.encolar(nodo_origen.get_valor_vertice())
        self.__obtener_ruta_corta_recursiva(Vertice(destino), cola_ruta)'''



    def __obtener_ruta_corta_recursiva(self, destino: str, nodos_visitados: Cola, nodos: Cola) -> Vertice:
        vertice_origen: Vertice = nodos.des_encolar().get_valor_vertice()
        if vertice_origen.get_valor() == destino:
            nodos_visitados.encolar(vertice_origen)
            return vertice_origen
        
        nodo_aux: NodoCola[Vertice] = vertice_origen.get_vecinos().get_inicio()
        while nodo_aux != None:
            if not self.__is_vecino_visitado(nodos_visitados, nodo_aux.get_valor_vertice()):
                peso: int = nodo_aux.get_valor_vertice().get_peso()
                vertice_vecino: Vertice = copy(self.__buscar_vertice(nodo_aux.get_valor_vertice().get_valor()))
                vertice_vecino.set_peso(peso)
                vertice_vecino.actualizar_peso_acumulado(vertice_origen.get_peso_acumulado() + peso)
                vertice_vecino.set_padre(vertice_origen)
                nodos.encolar(vertice_vecino)

            nodo_aux = nodo_aux.get_siguiente()
        nodos.ordenar()
        nodos_visitados.encolar(vertice_origen)
        return self.__obtener_ruta_corta_recursiva(destino, nodos_visitados, nodos)



    '''def __obtener_ruta_corta_recursiva(self, destino: Vertice, cola_ruta: Cola):
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
            inicio = inicio.get_siguiente()'''
    


    def __is_vecino_visitado(self, cola_nodos_visitados: Cola, valor: Vertice) -> bool:
        resultado: NodoCola = cola_nodos_visitados.buscar(valor.get_valor())
        return resultado != None



    def __buscar_vertice(self, valor: str) -> Vertice:
        nodo_aux: NodoLista[Vertice] = self.__lista_vertices.get_inicio()
        while nodo_aux != None:
            if nodo_aux.get_valor_vertice().get_valor() == valor:
                return nodo_aux.get_valor_vertice()
            
            nodo_aux = nodo_aux.get_siguiente()
        return None