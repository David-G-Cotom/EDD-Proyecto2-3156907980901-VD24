from ..models.Cliente import Cliente
from ..models.Vehiculo import Vehiculo
from ..models.Ruta import Ruta
from ..ArbolB.ArbolB import ArbolB
from ..ListaCircularDobleEnlazada.ListaClientes import ListaClientes
from ..Grafo.ListaAdyacencia import ListaAdyacencia
from tkinter import messagebox

class FileControl:
    def __init__(self):
        pass



    def procesar_clientes(self, contenido: str, lista_clientes: ListaClientes):
        print("PROCESANDO CLIENTES...")
        lineas: list[str] = contenido.split(";")
        for linea in lineas:
            if linea.__contains__("\n"):
                linea = linea.replace("\n", "")
            if linea != "":
                contenido: list[str] = linea.split(",")
                cliente: Cliente = Cliente(int(contenido[0]), contenido[1], contenido[2], contenido[3], int(contenido[4]), contenido[5])
                lista_clientes.insertar_cliente(cliente)
        messagebox.showinfo("EXITO!!!", "Carga de Clientes Realizado Exitosamente")



    def procesar_vehiculos(self, contenido: str, arbol_vehiculos: ArbolB):
        print("PROCESANDO VEHICLUOS...")
        lineas: list[str] = contenido.split(";")
        for linea in lineas:
            if linea.__contains__("\n"):
                linea = linea.replace("\n", "")
            if linea != "":
                contenido: list[str] = linea.split(":")
                vehiculo: Vehiculo = Vehiculo(contenido[0], contenido[1], int(contenido[2]), float(contenido[3]))
                arbol_vehiculos.insertar_vehiculo(vehiculo)
        messagebox.showinfo("EXITO!!!", "Carga de Vehiculos Realizado Exitosamente")



    def procesar_rutas(self, contenido: str, lista_adyacente: ListaAdyacencia):
        print("PROCESANDO RUTAS...")
        lineas: list[str] = contenido.split("%")
        for linea in lineas:
            if linea.__contains__("\n"): linea = linea.replace("\n", "")
            if linea.__contains__(" "): linea = linea.replace(" ", "")
            if linea != "":
                contenido: list[str] = linea.split("/")
                ruta: Ruta = Ruta(contenido[0], contenido[1], int(contenido[2]))
                lista_adyacente.insertar(ruta)
        messagebox.showinfo("EXITO!!!", "Carga de Rutas Realizado Exitosamente")