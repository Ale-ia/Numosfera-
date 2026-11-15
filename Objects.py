from abc import ABC, abstractmethod

class ObjetoCombinatorio(ABC):
    clave = ""
    descripcion = ""

    @abstractmethod
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ObjetoCombinatorio):
            return False
        return self.clave == otro.clave

class Seleccion(ObjetoCombinatorio):
    def __init__(self):
        self.elementos = set()

class Arreglo(ObjetoCombinatorio):
    def __init__(self):
        self.elementos = []

class Eleccion(ObjetoCombinatorio):
    def __init__(self):
        self.elementos = []
