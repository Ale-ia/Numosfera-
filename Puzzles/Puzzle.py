from abc import ABC, abstractmethod

class Puzzle(ABC):

    def __init__(self, titulo, pistas, explicacion, respuesta, objeto):
        self.titulo = titulo
        self._pistas = pistas
        self.intentos = 0
        self._explicacion = explicacion
        self._respuesta = respuesta
        self._objeto = objeto
        self._completado = False

    @abstractmethod
    def aplicar(self, accion):
        pass

    @abstractmethod
    def estaResuelto(self):
        pass

    @abstractmethod
    def mostrarPista(self):
        pass

    @abstractmethod
    def mostrarExplicacion(self):
        pass

