import Cliente, Vehiculo, Ruta;

class Viaje:
    def __init__(self, origen: str, destino: str, fecha: str, cliente: Cliente, vehiculo: Vehiculo, ruta: Ruta):
        self.__origen: str = origen
        self.__destino: str = destino
        self.__fecha: str = fecha
        self.__cliente: Cliente = cliente
        self.__vehiculo: Vehiculo = vehiculo
        self.__ruta: Ruta = ruta



    def get_origen(self) -> str:
        return self.__origen

    def set_origen(self, origen: str) -> None:
        self.__origen = origen

    

    def get_destino(self) -> str:
        return self.__destino
    
    def set_destino(self, destino: str) -> None:
        self.__destino = destino



    def get_fecha(self) -> str:
        return self.__fecha
    
    def set_fecha(self, fecha: str) -> None:
        self.__fecha = fecha



    def get_cliente(self) -> Cliente:
        return self.__cliente
    
    def set_cliente(self, cliente: Cliente) -> None:
        self.__cliente = cliente



    def get_vehiculo(self) -> Vehiculo:
        return self.__vehiculo

    def set_vehiculo(self, vehiculo: Vehiculo) -> None:
        self.__vehiculo = vehiculo

    

    def get_ruta(self) -> Ruta:
        return self.__ruta
    
    def set_ruta(self, ruta: Ruta) -> None:
        self.__ruta = ruta