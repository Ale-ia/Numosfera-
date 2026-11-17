
from Puzzles.puzzles import PuzzleDisfraces
from objects import Seleccion, Eleccion, Arreglo
from conteo import generar_elecciones

catalogo = {
    "camisa": ["roja", "azul"],
    "pantalon": ["negro", "blanco"],
    "zapatos": ["tenis", "botas"]
}

puzzle = PuzzleDisfraces(
    "Disfraces",
    ["Prueba combinar una opción de cada categoría."],
    "Cada atuendo se construye escogiendo una opción por categoría.",
    catalogo
)

print(puzzle.total)
# 8

eleccion1 = Eleccion({
    "camisa": "roja",
    "pantalon": "negro",
    "zapatos": "tenis"
})

eleccion2 = Eleccion({
    "camisa": "roja",
    "pantalon": "negro",
    "zapatos": "tenis"
})

eleccion3 = Eleccion({
    "camisa": "verde",
    "pantalon": "negro",
    "zapatos": "tenis"
})

print(puzzle.procesar_entrada(eleccion1))
# NUEVA

print(puzzle.procesar_entrada(eleccion2))
# REPETIDA

print(puzzle.procesar_entrada(eleccion3))
# INVALIDA

for eleccion in puzzle._generar_posibilidades():
    print(eleccion.descripcion())
     
