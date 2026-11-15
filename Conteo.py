from itertools import chain, combinations, permutations

def generar():
    pass
def cota_superior():
    pass
def determine_subsets(conjunto):
    items = list(conjunto)
    subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))
    subsets = [set(s) for s in subsets]
    return subsets

def determine_sized_subsets(subsetSize, conjunto):
    sizedSubsets = set()
    for element in determine_subsets(conjunto):
        if len(element) == subsetSize:
            sizedSubsets.add(frozenset(element))
    return sizedSubsets

def determine_arrangements(list):
        arrangements = permutations(list)
        return arrangements
