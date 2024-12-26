from .ListaClientes import ListaClientes
from .NodoListaDoble import NodoListaDoble
import os

class ReporteListaDoble:
    def __init__(self, lista_doble: ListaClientes):
        self.__lista_doble: ListaClientes = lista_doble



    def generar_reporte(self) -> None:
        dot: str = "digraph {\nrankdir=LR;\nnode[shape=box];\n"
        if not self.__lista_doble.is_vacia():
            nodo_aux: NodoListaDoble = self.__lista_doble.get_inicio()
            while True:
                dot += f'"{nodo_aux.get_cliente().get_dpi()}\n'
                dot += f'{nodo_aux.get_cliente().get_nombre()}"->\n'
                nodo_aux = nodo_aux.get_siguiente()
                if nodo_aux == self.__lista_doble.get_inicio(): break

            if self.__lista_doble.get_inicio() != self.__lista_doble.get_fin():
                dot += f'"{self.__lista_doble.get_inicio().get_cliente().get_dpi()}\n'
                dot += f'{self.__lista_doble.get_inicio().get_cliente().get_nombre()}"->\n'

            nodo_aux = self.__lista_doble.get_fin()
            while True:
                dot += f'"{nodo_aux.get_cliente().get_dpi()}\n'
                dot += f'{nodo_aux.get_cliente().get_nombre()}"->\n'
                nodo_aux = nodo_aux.get_anterior()
                if nodo_aux.get_anterior() == self.__lista_doble.get_fin(): break

            dot += f'"{nodo_aux.get_cliente().get_dpi()}\n'
            dot += f'{nodo_aux.get_cliente().get_nombre()}";'

        dot += "\n}"
        with open('./reports/ListaCircularDoble.txt', 'w') as file:
            file.write(dot)

        resultado: int = os.system(f"dot -Tpng reports\\ListaCircularDoble.txt -o reports\\ListaCircularDoble.png")
        if resultado == 0:
            print("Reporte generado exitosamente!!!")