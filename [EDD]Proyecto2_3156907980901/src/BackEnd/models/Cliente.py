class Cliente:
    def __init__(self, dpi: int, nombre: str, apellido: str, genero: str, telefono: int, direccion: str):
        self.__dpi: int = dpi
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__genero: str = genero
        self.__telefono: int = telefono
        self.__direccion: str = direccion



    def get_dpi(self) -> int:
        return self.__dpi

    def set_dpi(self, dpi: int) -> None:
        self.__dpi = dpi

    

    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre



    def get_apellido(self) -> str:
        return self.__apellido
    
    def set_apellido(self, apellido: str) -> None:
        self.__apellido = apellido



    def get_genero(self) -> str:
        return self.__genero
    
    def set_genero(self, genero: str) -> None:
        self.__genero = genero



    def get_telefono(self) -> int:
        return self.__telefono
    
    def set_telefono(self, telefono: int) -> None:
        self.__telefono = telefono



    def get_direccion(self) -> str:
        return self.__direccion
    
    def set_direccion(self, direccion: str) -> None:
        self.__direccion = direccion