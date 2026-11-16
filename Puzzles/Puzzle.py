from abc import ABC, abstractmethod
class Puzzle(ABC):
    def __init__(self, titulo, pistas, explicacion, respuesta, objeto):
        self._titulo = titulo
        self._pistas = pistas
        self._intentos = 0
        self._pistas_usadas = 0
        self._explicacion = explicacion
        self._completado = False
        self._respuesta = respuesta
        self.objeto = objeto
        self.opcionesContadas = set()

    def obtener_pista(self):
        return random.choice(self._pistas)

    def obtener_explicacion(self):
        return self._explicacion

    def esta_resuelto(self):
        pass

    def registrar_intento(self):
        self._intentos += 1

    @abstractmethod
    def procesar_entrada(self, entrada):
        pass