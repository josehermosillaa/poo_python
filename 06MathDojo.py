class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # tu código aquí
        operacion = self.result+num
        for n in nums:
            operacion+=n
        self.result += operacion    
        return self



    def subtract(self, num, *nums):
        # tu código aquí
        operacion = self.result-num
        for n in nums:
            operacion -= n
        self.result -= operacion    
        return self
md = MathDojo()
# para probar:copy
# x = md.subtract(3, 2).result
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
