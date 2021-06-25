# Imagina un juego donde puedes crear un zoológico y comenzar a criar diferentes tipos de animales. Digamos que por cada zoológico que crees puede haber varios animales diferentes. Comience creando una clase Animal y luego al menos 3 clases específicas de animales que hereden de Animal. (Tal vez leones, tigres y osos, ¡Dios mío!) Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad. La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal. También debe tener un método de alimentación que aumente la salud y la felicidad en 10.

# En al menos una de las clases de Animal child que ha creado, agregue al menos un atributo único. Dele a cada animal diferentes niveles predeterminados de salud y felicidad. Los animales también deben responder al método de alimentación con diferentes 
'''niveles de cambios en la salud y la felicidad'''
import random
def randint(min = 0, max = 100):
    if min == 0:
        num = round(max*(random.random()))
        
        return num
    else:
        num = round((max-min)*(random.random())+min)
        
        return num
# Una vez que haya probado sus diferentes animales y se sienta más cómodo con la herencia, cree una clase de zoológico para ayudar a manejar a todos sus animales.
class Animales:
    def __init__(self, nombre, edad,nivel_salud,nive_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.nivel_salud = randint()
        self.nivel_felicidad = randint()

    def display_info(self):
        print(f'''
        Nombre: {self.nombre}
        Edad  : {self.edad}
        Salud : {self.nivel_salud}%
        Felicidad: {self.nivel_felicidad}%''')
        
        return self
    
    def alimentar(self):
        print(f''' se esta alimentando a {self.name}, ñam ñam''')
        if self.nivel_salud+10 >100:
            self.nivel_salud = 100
        else:
            self.nivel_salud += 10
        if self.nivel_felicidad+10>100:
            self.nivel_felicidad = 100
        else:
            self.nivel_felicidad += 10
        print(f'''los nuevos parametros de {self.name} son''')
        self.display_info()


class Leon(Animales):
    def __init__(self, nombre, edad=10, nivel_salud=10, nivel_felicidad=20):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'viviparo'

class Oso(Animales):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'viviparo'
class Pinguino(Animales):
    def __init__(self, nombre, edad=9, nivel_salud=8, nivel_felicidad=6):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'Oviparo'


class Elefante(Animales):
    def __init__(self, nombre, edad, nivel_salud, nivel_felicidad):
        super().__init__(nombre, edad, nivel_salud, nivel_felicidad)
        self.reproduccion = 'viviparo'








# Una forma de armar este zoológico es haciendo lo siguiente:




class Zoo:
    def __init__(self, zoo_name):
        self.animales = []
        self.name = zoo_name
    def add_lion(self, nombre):
        self.animales.append( Leon(nombre) )
    def add_penguin(self, nombre):
        self.animales.append(Pinguino(nombre) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animales:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_penguin("Rey Julien")
zoo1.add_penguin("Rico")
zoo1.print_all_info()