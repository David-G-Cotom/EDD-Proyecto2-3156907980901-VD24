from .Lista.Lista import Lista

class Vertice:
    def __init__(self, valor: str, peso: int = 0, padre = None):
        self.__valor: str = valor
        self.__vecinos: Lista[Vertice] = Lista()
        self.__peso: int = peso
        self.__peso_acumulado: int = 0
        self.__padre: Vertice = padre



    def get_valor(self) -> str:
        return self.__valor

    def set_valor(self, value: str) -> None:
        self.__valor = value



    def get_vecinos(self) -> Lista:
        return self.__vecinos

    def set_vecinos(self, vecinos: Lista) -> None:
        self.__vecinos = vecinos



    def get_peso(self) -> int:
        return self.__peso

    def set_peso(self, peso: int) -> None:
        self.__peso = peso



    def get_peso_acumulado(self) -> int:
        return self.__peso_acumulado

    def set_peso_acumulado(self, peso_acumulado: int) -> None:
        self.__peso_acumulado = peso_acumulado

    def actualizar_peso_acumulado(self, peso_acumulado_anterior: int) -> None:
        self.__peso_acumulado += peso_acumulado_anterior



    def get_padre(self):
        return self.__padre

    def set_padre(self, padre) -> None:
        self.__padre = padre



    def __str__(self) -> str:
        nodo_aux = self.__vecinos.get_inicio()
        dot: str = ""
        while nodo_aux != None:
            dot += f"""edge[label={nodo_aux.get_valor_vertice().get_peso()} fontsize=5];
            {self.__valor} -> {nodo_aux.get_valor_vertice().get_valor()};\n\t"""
            nodo_aux = nodo_aux.get_siguiente()

        return dot
    


    def agregar_vecino(self, valor: str, peso: int) -> None:
        vecino: Vertice = Vertice(valor, peso)
        vecino.actualizar_peso_acumulado(peso)
        self.__vecinos.insertar_frente(vecino)