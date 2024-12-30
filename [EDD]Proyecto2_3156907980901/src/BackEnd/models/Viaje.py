import Cliente, Vehiculo, Ruta;
from ..Grafo.Lista.Lista import Lista
from ..Grafo.ListaAdyacencia import ListaAdyacencia

class Viaje:
    def __init__(self,id: int, origen: str, destino: str, cliente: Cliente, vehiculo: Vehiculo):
        self.__id: int = id
        self.__origen: str = origen
        self.__destino: str = destino
        #self.__fecha: str = fecha
        self.__cliente: Cliente = cliente
        self.__vehiculo: Vehiculo = vehiculo
        #self.__ruta: Ruta = ruta
        self.__ruta_corta: Lista = None



    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = id



    def get_origen(self) -> str:
        return self.__origen

    def set_origen(self, origen: str) -> None:
        self.__origen = origen

    

    def get_destino(self) -> str:
        return self.__destino
    
    def set_destino(self, destino: str) -> None:
        self.__destino = destino



    '''def get_fecha(self) -> str:
        return self.__fecha
    
    def set_fecha(self, fecha: str) -> None:
        self.__fecha = fecha'''



    def get_cliente(self) -> Cliente:
        return self.__cliente
    
    def set_cliente(self, cliente: Cliente) -> None:
        self.__cliente = cliente



    def get_vehiculo(self) -> Vehiculo:
        return self.__vehiculo

    def set_vehiculo(self, vehiculo: Vehiculo) -> None:
        self.__vehiculo = vehiculo

    

    '''def get_ruta(self) -> Ruta:
        return self.__ruta
    
    def set_ruta(self, ruta: Ruta) -> None:
        self.__ruta = ruta'''
    


    def get_ruta_corta(self) -> Lista:
        return self.__ruta_corta
    
    def set_ruta_corta(self, ruta_corta: Lista) -> None:
        self.__ruta_corta = ruta_corta



    def generar_ruta_corta(self, grafo: ListaAdyacencia):
        self.__ruta_corta = grafo.obtener_ruta_corta(self.__origen, self.__destino)