from Lista.Lista import Lista

class Vertice:
    def __init__(self, value: int):
        self.__value = value
        self.__vecinos: Lista = Lista()



    def get_value(self) -> int:
        return self.__value

    def set_value(self, value: int) -> None:
        self.__value = value



    def get_vecinos(self) -> Lista:
        return self.__vecinos

    def set_vecinos(self, vecinos: Lista) -> None:
        self.__vecinos = vecinos