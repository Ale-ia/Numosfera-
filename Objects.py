from abc import ABC, abstractmethod

class ObjetoCombinatorio(ABC):
    clave = 0
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ObjetoCombinatorio):
            return False
        return self.clave == otro.clave

class Seleccion(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.thisclave = self.clave
        self.clave += 1
        self.elementos = set(elementos)

class Arreglo(ObjetoCombinatorio):
    def __init__(self, elementos):
        self.thisclave = self.clave
        self.clave += 1
        self.elementos = list(elementos)

class Eleccion(ObjetoCombinatorio):
    def __init__(self):
        self.thisclave = self.clave
        self.clave += 1
        self.elementos = []
