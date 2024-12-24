from ..models.Cliente import Cliente
from ..models.Vehiculo import Vehiculo
from ..models.Ruta import Ruta
from ..ArbolB.ArbolB import ArbolB
from ..ListaCircularDobleEnlazada.ListaClientes import ListaClientes

class FileControl:
    def __init__(self):
        pass



    def procesar_clientes(self, contenido: str, lista_clientes: ListaClientes):
        print("PROCESANDO CLIENTES...")
        lineas: list[str] = contenido.split(";")
        for linea in lineas:
            contenido: list[str] = linea.split(",")
            cliente: Cliente = Cliente(contenido[0], contenido[1], contenido[2], contenido[3], contenido[4], contenido[5])
            lista_clientes.insertar_cliente(cliente)
            print(cliente)
        print("PROCESO DE CLIENTES TERMINADO")



    def procesar_vehiculos(self, contenido: str, arbol_vehiculos: ArbolB):
        print("PROCESANDO VEHICLUOS...")
        lineas: list[str] = contenido.split(";")
        for linea in lineas:
            contenido: list[str] = linea.split(":")
            vehiculo: Vehiculo = Vehiculo(contenido[0], contenido[1], contenido[2], contenido[3])
            arbol_vehiculos.insertar_vehiculo(vehiculo)
            print(vehiculo)
        print("PROCESO DE VEHICLUOS TERMINADO")



    def procesar_rutas(self, contenido: str):
        print("PROCESANDO RUTAS...")
        lineas: list[str] = contenido.split("%")
        for linea in lineas:
            contenido: list[str] = linea.split("/")
            ruta: Ruta = Ruta(contenido[0], contenido[1], contenido[2])
            #AGREGARLO AL GRAFO
        print("PROCESO DE RUTAS TERMINADO")