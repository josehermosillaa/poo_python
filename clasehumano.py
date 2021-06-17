
class Humano(): #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion): #Definimos el atributo edad y nombre
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion # atributo de instancia ocupacion
        self.estado_civil = "soltero"
        self.hijo = 0
        self.familia = 1
        

    def presentar(self):
        print(f"Hola soy {self.nombre}, mi edad es {self.edad} y mi ocupacion es {self.ocupacion}")
    #podemos usar un metodo para contratar a pedro

    def contratar(self, cargo):
        #parametro nuevo asociado al puesto en que se contratará a pedro
        self.cargo = cargo
        print(f"{self.nombre} a sido contratado para el puesto de {self.cargo}")
        self.ocupacion = cargo
        return self

    def matrimonio(self,otro):
        print(f"{self.nombre} se ha casado con {otro.nombre}")
        self.estado_civil = "casado"
        otro.estado_civil = "casado"
        self.familia += 1
        otro.familia += 1
        return self
    
    def hijos(self,numero,otro):
        print(f"{self.nombre} tuvo {numero} hijo con {otro.nombre}")
        self.hijo += numero
        otro.hijo += numero
        self.familia += numero
        otro.familia += numero
        return self
    
    def circulo_familiar(self):
            print(f"la familia de {self.nombre} tiene {self.familia} integrantes")
            return self
    def bono(self):
        if self.ocupacion != 'Desocupado':
            print(f"no tiene derecho a bono")
        else:
            print(f"tiene derecho a bono")
        return self


pedro = Humano(31, "Pedro", "Desocupado") #Instancia
juanita = Humano(28,"Juanita","Desocupado")
francisco = Humano(29,"Francisco","Profesor")
#LLamada al metodo
pedro.presentar()
print(pedro.estado_civil)
print(juanita.estado_civil)
pedro.contratar("Obrero")
pedro.matrimonio(juanita)
print(pedro.estado_civil)
print(juanita.estado_civil)
pedro.circulo_familiar()
francisco.circulo_familiar()
francisco.bono()
juanita.bono()
