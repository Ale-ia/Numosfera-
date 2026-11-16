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
        self._pares = tuple(sorted(elementos.items()))
        self.clave = self._pares
    @property
    def elementos(self):
        return dict(self._pares)
    @property
    def categorias(self):
        return tuple(categoria for categoria, opcion in self._pares)
    def opcion_de(self, categoria):
        return dict(self._pares)[categoria]
    def descripcion(self):
        return ", ".join(
            f"{categoria}: {opcion}"
            for categoria, opcion in self._pares
        )

