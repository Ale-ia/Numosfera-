class Path:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puzzles = {}
        self.puzzlesCompletados = []
        self.temasAprendidos = []

    def completarPuzzle(self, puzzle):
        self.puzzlesCompletados.append(puzzle)