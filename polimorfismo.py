# Usaremos la clase Person para demostrar el polimorfismo
# en el que varias clases heredan de la misma clase pero se comportan de diferentes maneras
class Person:
    def pay_bill(self):
        raise NotImplementedError("No esta implementada la funcion")
# Millionaire hereda de Persona

class Millionaire(Person):
    def pay_bill(self):
        print("Millonario - Tome, paguese.")
# Grad Student también hereda de la clase Persona

class GradStudent(Person):
    def pay_bill(self):
        print("Estudiante - No tengo plata, puedo lavar platos?")

class Conductor(Person):
    def pay_bill(self):
        print("Conductor - Me arranco...")

class Secretario(Person):
    pass        

try:

    pancho = Millionaire()
    adrian = Conductor()
    jose = GradStudent()

    listaPersonas = [pancho, adrian, jose]


    lala = Secretario()
    lala.pay_bill()

except NotImplementedError as err :
    print("ERROR: ",err)
except Exception as err :
    print("ERROR: ",err)
finally:
    print("Se ejecuta para bien o para mal.")