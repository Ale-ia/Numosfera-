from itertools import chain, combinations, permutations

class Enumerador:
    def generar(self):
        pass
    def cota_superior(self):
        pass
    def determineSubsets(self, set):
        items = list(set)
        subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))
        subsets = [set(s) for s in subsets]
        return subsets

    def determineSizedSubsets(self, subsetSize, set):
        sizedSubsets = set()
        for element in self.determineSubsets(set):
            if len(element) == subsetSize:
                sizedSubsets.add(element)
        return sizedSubsets

    def determineArrangements(self, list):
            arrangements = permutations(self.list)
            return arrangements