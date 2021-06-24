''' anulacion al definir la funcion con el mismo nombre que la del padre en la clase hijo, la que hereda
class Parent:
    def method_a(self):
        print("invocando PARENT method_a!")


class Child(Parent):
    def method_a(self):
        print("invocando CHILD method_a!")


dad = Parent()
son = Child()
dad.method_a()
son.method_a()  # ¡nota que esto anula el método Parent!'' '''

# Usaremos la clase Person para demostrar el polimorfismo
# en el que varias clases heredan de la misma clase pero se comportan de diferentes maneras


class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire hereda de Persona


class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")


# Grad Student también hereda de la clase Persona
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")
