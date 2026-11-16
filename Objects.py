from abc import ABC
class ObjetoCombinatorio(ABC):
    clave = 0
    def __eq__(self, otro: object) -> bool:
        return type(self) is type(otro) and self.clave == otro.clave

class Seleccion(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.elementos = frozenset(elementos)
        self.clave = self.elementos

class Arreglo(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.elementos = tuple(elementos)
        self.clave = self.elementos

class Eleccion(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.elementos = {elementos}
        self.clave = self.elementos
