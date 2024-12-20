class Ruta:
    def __init__(self, origen: str, destino: str, tiempo: int):
        self.__origen: str = origen
        self.__destino: str = destino
        self.__tiempo: int = tiempo



    def get_origen(self) -> str:
        return self.__origen

    def set_origen(self, origen: str) -> None:
        self.__origen = origen

    

    def get_destino(self) -> str:
        return self.__destino
    
    def set_destino(self, destino: str) -> None:
        self.__destino = destino



    def get_tiempo(self) -> str:
        return self.__tiempo
    
    def set_tiempo(self, tiempo: str) -> None:
        self.__tiempo = tiempo