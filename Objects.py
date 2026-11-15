from abc import ABC, abstractmethod
from itertools import chain, combinations, permutations

class ObjetoCombinatorio(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass
    @abstractmethod
    def clave(self):
        pass
    def __eq__(self, otro: object) -> bool:
        pass

class Seleccion(ObjetoCombinatorio):
    def __init__(self):
        self.set = set()
        self.subsets = set()
        self.sizedSubsets = set()

    def determineSubsets(self):
        items = list(self.set)
        subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))
        subsets = [set(s) for s in subsets]
        return subsets

    def determineSizedSubsets(self, subsetSize):
        sizedSubsets = set()
        for element in self.subsets:
            if len(element) == subsetSize:
                sizedSubsets.add(element)
        return sizedSubsets

class Arreglo(ObjetoCombinatorio):
    def __init__(self):
        self.list = []

    def determineArrangements(self):
        arrangements = permutations(self.list)
        return arrangements

class Eleccion(ObjetoCombinatorio):
    def __init__(self):
        self.iterable = []
