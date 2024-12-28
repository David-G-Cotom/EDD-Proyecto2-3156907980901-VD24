from .ArbolB import ArbolB
from .NodoArbolB import NodoArbolB
import os
from tkinter import Frame, Label
from PIL import Image, ImageTk


class ReporteArbolB:
    def __init__(self, arbol_b: ArbolB):
        self.__arbol_b: ArbolB = arbol_b



    def generar_reporte(self, formulario_frame: Frame) -> None:
        dot: str = '''digraph G {\n\tbgcolor="#1a1a1a";
            fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false
            node [shape=record width=1.2 style=filled fillcolor="#313638" fontcolor=white];
            edge [fontcolor=white color="#0070c9"];\n\t'''
        dot += self.__imprimir_contenido(self.__arbol_b.get_raiz())
        dot += "\n}"
        with open('./reports/ArbolB.txt', 'w') as file:
            file.write(dot)

        resultadoPNG: int = os.system(f"dot -Tpng reports\\ArbolB.txt -o reports\\ArbolB.png")
        resultadoPDF: int = os.system(f"dot -Tpdf reports\\ArbolB.txt -o reports\\ArbolB.pdf")
        if resultadoPNG == 0 and resultadoPDF == 0:
            print("Reporte generado exitosamente!!!")
            self.__mostrar_imagen(formulario_frame)
    


    def __imprimir_contenido(self, nodo: NodoArbolB, id: list[int] = [0]) -> str:
        raiz_sub_arbol: NodoArbolB = nodo
        contenido_arbol = f'n{id[0]}[label="'
        contador: int = 0
        for clave in raiz_sub_arbol.get_claves():
            if contador == len(raiz_sub_arbol.get_claves())-1:
                contenido_arbol += f"<f{contador}>|{clave.get_placa()}|<f{contador + 1}>"
                break
            contenido_arbol += f"<f{contador}>|{clave.get_placa()}|"
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
    


    def __mostrar_imagen(self, formulario_frame: Frame) -> None:
        for widget in formulario_frame.winfo_children():
            widget.destroy()
        img = Image.open('./reports/ArbolB.png')
        pimg = ImageTk.PhotoImage(img)
        formulario_frame.pimg = pimg
        Label(formulario_frame, image=pimg).grid(row=0)
        print("Imagen Cargada Exitosamente!!!")