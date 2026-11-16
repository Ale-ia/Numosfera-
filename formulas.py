from math import factorial, comb

def calcular_combinacion(n,k):
    return comb(n,k)

def calcular_potenciacion(n,k):
    return n**k

def calcular_producto(cantidades):
    total = 1
    for cantidad in cantidades:
        total *= cantidad
    return total
    
def calcular_multinomial(frecuencias):
    n = sum(frecuencias)
    denominador = 1
    for frecuencia in frecuencias:
        denominador *= factorial(frecuencia)
    return factorial(n) // denominador

def calcular_inclusion_exclusion(a,b):
    intersection = set()
    for element in a:
        if element in b:
            intersection.add(element)
    return len(a)+len(b)-len(intersection)