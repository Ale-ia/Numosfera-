from abc import ABC
class ObjetoCombinatorio(ABC):
    clave = 0
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ObjetoCombinatorio):
            return False
        return self.clave == otro.clave

class Seleccion(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.thisclave = self.clave
        self.clave = frozenset(elementos)
        self.elementos = set(elementos)

class Arreglo(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.thisclave = self.clave
        self.clave = tuple(elementos)
        self.elementos = list(elementos)

class Eleccion(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.thisclave = self.clave
        self.clave = tuple(elementos)
        self.elementos = list(elementos)
