class Producto:
    def __init__(self):
        self.cosoto = 0

    def precio(self):
        raise NotImplementedError("No esta implementada la función PRECIO")

class Libro(Producto):
    def __init__(self):
        super().__init__()
        self.autor = ""
    def precio(self):
        if self.autor == "":
            return self.costo*2.50
        return self.costo*1.30

class Alimento(Producto):
    def __init__(self):
        super().__init__()
        self.marca = ""
        self.tipo =""

class Adorno(Producto):
    def __init__(self):
        super().__init__()
        self.descripcion = ""
try:

    inferno = Libro()
    inferno.costo = 1000

    print("el precio del libro SIN AUTOR es: ",inferno.precio())
    inferno.autor = "Dan Brown"
    print("el precio del libro CON AUTOR es:",inferno.precio())

    tomate = Alimento()
    cenicero = Adorno()
    print("el precio del tomate es:",tomate.precio())
except Exception as err:
    print("Err:",err)