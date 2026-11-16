from itertools import chain, combinations, permutations

def determine_subsets(conjunto):
    items = list(conjunto)
    subsets = chain.from_iterable(combinations(items, r) for r in range(len(items) + 1))
    subsets = [set(s) for s in subsets]
    return subsets

def determine_sized_subsets(conjunto, subset_size):
    sized_subsets = set()
    for element in determine_subsets(conjunto):
        if len(element) == subset_size:
            sized_subsets.add(frozenset(element))
    return sized_subsets

def determine_arrangements(list):
        arrangements = set(permutations(list))
        return arrangements

def generar_elecciones(catalogo):

    categorias = tuple(catalogo.keys())
    opciones = [
        catalogo[categoria]
        for categoria in categorias
    ]
    for combinacion in product(*opciones):

        elementos = dict(zip(categorias, combinacion))

        yield Eleccion(elementos)
