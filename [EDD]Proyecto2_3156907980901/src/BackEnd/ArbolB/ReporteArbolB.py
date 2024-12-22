from .ArbolB import ArbolB
from .NodoArbolB import NodoArbolB
import os


class ReporteArbolB:
    def __init__(self, arbol_b: ArbolB):
        self.__arbol_b: ArbolB = arbol_b



    def generar_reporte(self) -> None:
        dot: str = '''
                digraph G {\n\tbgcolor="#1a1a1a";\n\t
                fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false\n\t
                node [shape=record width=1.2 style=filled fillcolor="#313638" fontcolor=white colortransparent];\n\t
                edge [fontcolor=white color="#0070c9"];\n\t
                '''
        dot += self.__imprimir_contenido(self.__arbol_b.get_raiz())
        dot += "\n}"
        with open('./reports/ArbolB.txt', 'w') as file:
            file.write(dot)

        resultado: int = os.system(f"dot -Tpng reports\\ArbolB.txt -o reports\\ArbolB.png")
        if resultado == 0:
            print("Reporte generado exitosamente!!!")
    


    def __imprimir_contenido(self, nodo: NodoArbolB, id: list[int] = 0) -> str:
        raiz_sub_arbol: NodoArbolB = nodo
        contenido_arbol = f'n{id[0]}[label="'
        contador: int = 0
        for clave in raiz_sub_arbol.get_claves():
            if contador == len(raiz_sub_arbol.get_claves()-1):
                contenido_arbol += f"<f{contador}>|{clave}|<f{contador + 1}>"
                break
            contenido_arbol += f"<f{contador}>|{clave}|"
            contador += 1
        contenido_arbol += '"];\n\t'

        contador: int = 0
        id_padre: int = id[0]
        for sub_nodo in raiz_sub_arbol.get_hijos():
            contenido_arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            id[0] += 1
            contenido_arbol += self.__imprimir_contenido(sub_nodo, id)
            contador += 1

        return contenido_arbol