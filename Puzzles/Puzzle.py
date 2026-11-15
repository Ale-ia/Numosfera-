from abc import ABC
class Puzzle(ABC):
    titulo = ""
    pistas = []
    intentos = 0

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

