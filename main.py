
from Puzzles.puzzles import PuzzleApretones
from objects import Seleccion
from conteo import determine_sized_subsets

objeto1 = Seleccion(("Ana", "Beto", "Carmen"))
puzzle1 = PuzzleApretones("Apretones de manos", ["Pista 1", "Pista 2"], "Explicación del puzzle", "3", objeto1)

opcionesContadas = set()

def compararOpcionesContadas(opcion):
    global opcionesContadas

    if opcion in opcionesContadas:
        print(f"La opción {opcion} ya había sido contada, intenta otra opción.")
    elif opcion in determine_sized_subsets(2, objeto1.elementos):
        opcionesContadas.add(opcion)
        print(f"La opción {opcion} es válida y ha sido contada.")

print("Bienvenido al puzzle de Apretones de manos.")
print("Dado el grupo de personas Ana, Beto y Carmen, ¿cuántos apretones de manos se pueden dar?")
print("Ingresa un apretón de manos separado por un espacio para contarlo, por ejemplo: Ana Beto\n")

while len(opcionesContadas) < 3:
    user_input = set(input().split())
    compararOpcionesContadas(frozenset(user_input))
    print("Llevas contadas las siguientes opciones válidas:", opcionesContadas)

print("¡Felicidades! Has contado todas las opciones válidas.")
     
