class MathDojo:
    def __init__(self):
        self.result = 0
        self.numeros = []

    def add(self, num, *nums):
        # tu código aquí
        self.numeros.append(num)
        for n in nums:
            self.numeros.append(n)
            num+=n
        print(f'-->se suma {num}')
        self.result += num  
        print(f'el resultado despues de la operacion es : {self.result}')
        return self



    def subtract(self, num, *nums):
        # tu código aquí
        self.numeros.append(-num)
        for n in nums:
            self.numeros.append(-n)
            num += n
        print(f'-->se resta {num}')
        self.result -= num
        print(f'el resultado despues de la operacion es : {self.result}')
        return self

    def verlista(self):
        print(self.numeros)
        return self

    def desviacion_estandar(self):
        n = len(self.numeros)
        promedio = self.result/n
        # print(f'el promedio sera : {promedio}')
        for i in range(len(self.numeros)):
            self.numeros[i]-=promedio
            self.numeros[i] = self.numeros[i]**2
        sumacuadrada = 0
        for num in self.numeros:
            sumacuadrada+=num
        # print(f'la suma al cuadrado es :{sumacuadrada}')
        desviacion_estandar = (sumacuadrada/n-1)**0.5
        print(f'la desviacion estandar de los numeros ingresados es: {desviacion_estandar}')
        return self
        
            


if __name__ == '__main__':
    md = MathDojo()
    # para probar:copy
    x = md.add(2).add(2, 5, 1).subtract(3, 2)
    md.desviacion_estandar()
    md.verlista()
    md1 = MathDojo()
    y = md1.add(8).add(9,15,11).add(34,2)
    # corre cada uno de los metodos algunos mas veces y valida el resultado!

    md2 = MathDojo()
    z= md2.subtract(-3).subtract(0,5,4).subtract(-3,5,6,7)

