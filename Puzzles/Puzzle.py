from abc import ABC

class Puzzle(ABC):
    titulo = ""
    _pistas = []
    intentos = 0
    explicacion = ""
    _respuesta = ""
    _completado = False

    def __init__(self, titulo, pistas, explicacion, respuesta):
        self.titulo = titulo
        self.pistas = pistas
        self.intentos = 0
        self.explicacion = explicacion
        self.respuesta = respuesta
        self.completado = False

    @abstractmethod
    def aplicar(accion):
        pass

    @abstractmethod
    def estaResuelto():
        pass

    @abstractmethod
    def mostrarPista():
        pass

    @abstractmethod
    def mostrarExplicacion():
        pass

