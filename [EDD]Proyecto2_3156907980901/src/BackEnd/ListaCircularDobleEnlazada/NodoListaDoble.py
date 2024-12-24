from ..models.Cliente import Cliente

class NodoListaDoble:
    def __init__(self, cliente: Cliente):
        self.__siguiente: NodoListaDoble = None
        self.__anterior: NodoListaDoble = None
        self.__cliente: Cliente = cliente



    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, siguiente) -> None:
        self.__siguiente = siguiente

    

    def get_anterior(self):
        return self.__anterior
    
    def set_anterior(self, anterior) -> None:
        self.__anterior = anterior



    def get_cliente(self) -> Cliente:
        return self.__cliente
    
    def set_cliente(self, cliente: Cliente) -> None:
        self.__cliente = cliente