from .ListaAdyacencia import ListaAdyacencia
from .Vertice import Vertice
from .Lista.NodoLista import NodoLista
import os

class ReporteGrafo:
    def __init__(self, lista_adyacente: ListaAdyacencia):
        self.__lista_adyacente: ListaAdyacencia = lista_adyacente



    def generar_reporte(self) -> None:
        dot = self.__imprimir()
        with open('./reports/Grafo.txt', 'w') as file:
            file.write(dot)

        resultado: int = os.system(f"neato -Tpng reports\\Grafo.txt -o reports\\Grafo.png")
        if resultado == 0:
            print("Reporte generado exitosamente!!!")



    def __imprimir(self) -> str:
        dot: str = '''digraph G {\n\tbgcolor="#1a1a1a";
            node [shape=circle fixedsize=shape  width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white color=transparent];
            edge [arrowhead=none fontcolor=white color="#ff5400"];\n\t'''
        nodo_aux: NodoLista[Vertice] = self.__lista_adyacente.get_lista_vertices().get_inicio()
        while nodo_aux != None:
            if nodo_aux != None:
                dot += str(nodo_aux.get_valor_vertice())

            nodo_aux = nodo_aux.get_siguiente()
        dot += "}"
        return dot