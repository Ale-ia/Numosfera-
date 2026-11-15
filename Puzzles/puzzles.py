class PuzzleApretones(Puzzle):
    def __init__(self, n, k):
        super().__init__(titulo, pistas, explicacion, respuesta)
        self.n = n
        self.k = k

class PuzzleLamparas(Puzzle):
    def __init__(self, n, k):
        super().__init__(titulo, pistas, explicacion, respuesta)
        self.n = n
        self.k = k

class PuzzleDisfraces(Puzzle):
    def __init__(self, n, k):
        super().__init__(titulo, pistas, explicacion, respuesta)
        self.n = n
        self.k = k

class PuzzleAnagramas(Puzzle):
    def __init__(self, palabra):
        super().__init__(titulo, pistas, explicacion, respuesta)
        self.palabra = palabra

class PuzzleInclusionExclusion(Puzzle):
    def __init__(self, a, b, intersection):
        super().__init__(titulo, pistas, explicacion, respuesta)
        self.a = a
        self.b = b
        self.intersection = intersection