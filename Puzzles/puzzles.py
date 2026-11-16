
from .Puzzle import Puzzle
from formulas import calcular_combinacion, calcular_multinomial, calcular_potenciacion, calcular_producto, calcular_inclusion_exclusion
from conteo import determine_sized_subsets, determine_subsets, determine_arrangements

#APRETONES(COMBINACIONES)

class PuzzleApretones(Puzzle):
    
    def __init__(self, titulo, pistas, explicacion, objeto, subset_size=2):
        super().__init__(titulo, pistas, explicacion, objeto)
        self.subsetSize = subset_size

    def es_valida(self, entrada):
        return entrada in self._generar_opciones()

    def procesar_entrada(self, entrada):
        if not self.es_valida(entrada):
            print("La entrada no es válida.")
        elif entrada in self.opcionesContadas:
            print(f"La opción {entrada} ya había sido contada, intenta otra opción.")
        else:
            self.opcionesContadas.add(entrada)
            print(f"La opción {entrada} es válida y ha sido contada.")
        self._esta_completo()

    def _generar_opciones(self):
        return determine_sized_subsets(self.objeto.elementos, self.subsetSize)

    def _calcular_total(self):
        return calcular_combinacion(len(self.objeto.elementos), self.subsetSize)

    def _esta_completo(self):
        if self.opcionesContadas == self._generar_opciones():
            self._completado = True
            print("¡Felicidades! Has contado todas las opciones válidas.")

    def pedir_respuesta(self):
        respuesta_usuario = input("Basándote en lo que has contado, ¿Cuántos apretones posibles hay? Ingresa tu respuesta: ")
        self.registrar_intento()
        if respuesta_usuario == self._respuesta:
            print("¡Correcto!")
            self._completado = True
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")

#LAMPARAS(POTENCIACION)(CASO ESPECIFICO DE PRODUCTO)

class PuzzleLamparas(Puzzle):
    def __init__(self, titulo, pistas, explicacion, respuesta, objeto):
        super().__init__(titulo, pistas, explicacion, respuesta, objeto)

    def es_valida(self, entrada):
        return entrada in self._generar_opciones()
    
    def procesar_entrada(self, entrada):
        #print("Teniendo en cuenta las lámparas, escribe solamente las lámparas que están ENCENDIDAS. Si no quieres que hayan lámparas encendidas, simplemente no escribas nada. Recuerda separar cada lámpara con un espacio.")
        if not self.es_valida(entrada):
            print("La opción ingresada no es válida. Asegúrate de ingresar lámparas válidas.")
        elif entrada in self.opcionesContadas:
            print(f"La opción {entrada} ya había sido contada, intenta otra opción.")
        else:
            self.opcionesContadas.add(entrada)
            print(f"La opción {entrada} es válida y ha sido contada.")

    def _generar_opciones(self):
        return determine_subsets(self.objeto.elementos)

    def _calcular_total(self):
        return calcular_potenciacion(len(2, self.objeto.elementos))  # Cada lámpara tiene 2 estados: encendida o apagada

    def _esta_completo(self):
        if self.opcionesContadas == self._generar_opciones():
            self._completado = True
            print("¡Felicidades! Has contado todas las opciones válidas.")

    def pedir_respuesta(self):
        respuesta_usuario = input("Basándote en lo que has contado, ¿Cuántas combinaciones posibles de lámparas hay? Ingresa tu respuesta: ")
        self.registrar_intento()
        if respuesta_usuario == self._respuesta:
            print("¡Correcto!")
            self._completado = True
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")

#DISFRACES(PRODUCTO)

class PuzzleDisfraces(Puzzle):
    def __init__(self, titulo, pistas, explicacion, respuesta, objeto, ):
        super().__init__(titulo, pistas, explicacion, respuesta, objeto)
        self.objeto = {
        "camisa": ["roja", "azul"],
        "pantalon": ["negro", "blanco"],
        "zapatos": ["tenis", "botas"]
        }

    def es_valida(self, entrada):
        camiseta = False
        pantalon = False
        zapatos = False
        for opcion in entrada:
            if not camiseta:
                if opcion in self.objeto["camisa"]:
                    camiseta = True
            if not pantalon:
                if opcion in self.objeto["pantalon"]:
                    pantalon = True
            if not zapatos:
                if opcion in self.objeto["zapatos"]:
                    zapatos = True
        return camiseta and pantalon and zapatos

    def procesar_entrada(self, entrada):
        if not self.es_valida(entrada):
            print("La opción ingresada no es válida. Asegúrate de ingresar disfraces válidos.")
        
    def _calcular_total(self):
        self._respuesta = calcular_producto(self.objeto)
        return calcular_producto(self.objeto)

    def _generar_posibilidades(self):
        pass

    def _esta_resuelto(self):
        if self.opcionesContadas == self._generar_opciones():
            self._completado = True
            print("¡Felicidades! Has contado todas las opciones válidas.")

#ANAGRAMAS(PERMUTACIONES)(CON REPETICION)

class PuzzleAnagramas(Puzzle):
    def __init__(self, titulo, pistas, explicacion, respuesta, objeto):
        super().__init__(titulo, pistas, explicacion, respuesta, objeto)

    def es_valida(self, entrada):
        return entrada in self._generar_opciones()

    def procesar_entrada(self, entrada):
        if not self.es_valida(entrada):
            print("La opción ingresada no es válida. Asegúrate de ingresar anagramas válidos.")
        elif entrada in self.opcionesContadas:
            print(f"La opción {entrada} ya había sido contada, intenta otra opción.")
        else:
            self.opcionesContadas.add(entrada)
            print(f"La opción {entrada} es válida y ha sido contada.")

    def _generar_opciones(self):
        return determine_arrangements(self.objeto)

    def _calcular_total(self):
        self._respuesta = calcular_multinomial(len(self.objeto))
        return self._respuesta

    def esta_resuelto(self):
        if self.opcionesContadas == self._generar_opciones():
            self._completado = True
            print("¡Felicidades! Has contado todas las opciones válidas.")

    def pedir_respuesta(self):
        respuesta_usuario = int(input("Basándote en lo que has contado, ¿Cuántos anagramas posibles hay? Ingresa tu respuesta: "))
        self.registrar_intento()
        if respuesta_usuario == self._respuesta:
            print("¡Correcto!")
            self._completado = True
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")

#INCLUSION-EXCLUSION

class PuzzleInclusionExclusion(Puzzle):
    def __init__(self, titulo, pistas, explicacion, respuesta, objeto1, objeto2):
        super().__init__(titulo, pistas, explicacion, respuesta, objeto1)
        self.objeto2 = objeto2

    def procesar_entrada(self, entrada):
        pass

    def pedir_respuesta(self):
        user_input = int(input("Cuenta la cantidad de elementos de la union de los conjuntos, y escribela a continuacion:"))
        self.registrar_intento()
        if user_input == len(self.objeto.elementos) +  len(self.objeto2.elementos):
            print("Revisa si estás contando más de una vez algún elemento. Inténtalo de nuevo.")
        elif user_input == calcular_inclusion_exclusion(self.objeto.elementos, self.objeto2.elementos):
            print("¡Correcto!")
            self._completado = True
        else:
            print("Respuesta incorrecta. Intenta de nuevo.")