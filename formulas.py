from math import factorial, comb

def calcular_combinacion(n,k):
    return comb(n,k)

def calcular_potenciacion(n,k):
    return n**k

def calcular_producto(categorias):
    total = 1
    for categoria in categorias:
        if categoria <= 0:
            return 0
        total = total * categoria
    return total
    
def calcular_multinomial(n):
    return factorial(n)

def calcular_inclusion_exclusion(a,b,intersection):
    return a+b-intersection