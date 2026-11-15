from abc import ABC, abstractmethod

class ObjetoCombinatorio(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass
    @abstractmethod
    def clave(self):
        pass
    def __eq__(otro) -> bool:
        pass

    class Seleccion(ObjetoCombinatorio):
        conjunto = {}

    class Arreglo(ObjetoCombinatorio):
        lista = []

    class Eleccion(ObjetoCombinatorio):
        iterable = []

