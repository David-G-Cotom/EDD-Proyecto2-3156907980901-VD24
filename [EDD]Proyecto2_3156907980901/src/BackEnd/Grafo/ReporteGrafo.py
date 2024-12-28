from .ListaAdyacencia import ListaAdyacencia
from .Vertice import Vertice
from .Lista.NodoLista import NodoLista
import os
from tkinter import Frame, Label
from PIL import Image, ImageTk
# from reportlab.graphics import renderPDF, renderPM
# from svglib.svglib import svg2rlg

class ReporteGrafo:
    def __init__(self, lista_adyacente: ListaAdyacencia):
        self.__lista_adyacente: ListaAdyacencia = lista_adyacente



    def generar_reporte(self, formulario_frame: Frame) -> None:
        dot = self.__imprimir()
        with open('./reports/Grafo.txt', 'w') as file:
            file.write(dot)

        resultadoPNG: int = os.system(f"neato -Tpng reports\\Grafo.txt -o reports\\Grafo.png")
        resultadoPDF: int = os.system(f"neato -Tpdf reports\\Grafo.txt -o reports\\Grafo.pdf")
        if resultadoPNG == 0 and resultadoPDF == 0:
            print("Reporte generado exitosamente!!!")
            self.__mostrar_imagen(formulario_frame)



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
    


    def __mostrar_imagen(self, formulario_frame: Frame) -> None:
        # drawing = svg2rlg("./reports/Grafo.svg")
        # renderPDF.drawToFile(drawing, "./reports/temp.pdf", fmt="PDF")
        for widget in formulario_frame.winfo_children():
            widget.destroy()
        img = Image.open('./reports/Grafo.png')
        pimg = ImageTk.PhotoImage(img)
        formulario_frame.pimg = pimg
        Label(formulario_frame, image=pimg).grid(row=0)
        print("Imagen Cargada Exitosamente!!!")
        # size = img.size
        # frame = Canvas(formulario_fram, width=size[0], height=size[1])
        # frame.pack()
        # frame.create_image(0, 0, anchor='nw', image=pimg)