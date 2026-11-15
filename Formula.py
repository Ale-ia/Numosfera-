from math import factorial, comb
class Formula:
    @staticmethod
    def calcularCombinacion(self,n,k):
        return comb(n,k)
    @staticmethod
    def calcularPotenciacion(self,n,k):
        return n**k
    @staticmethod
    def calcularProducto():
        pass
    @staticmethod
    def calcularMultinomial():
        pass
    def calcularInclusionExclusion(self,a,b,intersection):
        return a+b-intersection