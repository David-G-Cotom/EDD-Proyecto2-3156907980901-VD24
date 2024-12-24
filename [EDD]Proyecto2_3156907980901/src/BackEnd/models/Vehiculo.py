class Vehiculo:
    def __init__(self, placa: str, marca: str, modelo: int, precio: float):
        self.__placa: str = placa
        self.__marca: str = marca
        self.__modelo: int = modelo
        self.__precio: float = precio



    def get_placa(self) -> str:
        return self.__placa

    def set_placa(self, placa: str) -> None:
        self.__placa = placa

    

    def get_marca(self) -> str:
        return self.__marca
    
    def set_marca(self, marca: str) -> None:
        self.__marca = marca



    def get_modelo(self) -> int:
        return self.__modelo
    
    def set_modelo(self, modelo: int) -> None:
        self.__modelo = modelo



    def get_precio(self) -> float:
        return self.__precio
    
    def set_precio(self, precio: float) -> None:
        self.__precio = precio



    def __str__(self):
        return f"PLACA:{self.__placa} MARCA:{self.__marca} MODELO:{self.__modelo} PRECIO:{self.__precio}"